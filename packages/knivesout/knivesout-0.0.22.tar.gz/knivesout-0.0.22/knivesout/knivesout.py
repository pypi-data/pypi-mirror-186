#!/usr/bin/env python3
import ast
import asyncio
import atexit
import json
import os
import pprint
import sys
import time
from abc import ABC, abstractmethod
from signal import SIGTERM
from typing import List, Optional, Tuple

import codefast as cf
import fire
import pandas as pd
from codefast.asyncio import async_render
from codefast.io.osdb import osdb
from codefast.logger import get_logger
from pydantic import BaseModel


class Daemon(object):
    """A generic daemon class.
    Usage: subclass the Daemon class and override the run() method
    """

    def __init__(self,
                 pidfile,
                 stdin='/dev/null',
                 stdout='/dev/null',
                 stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError:
            sys.stderr.write("fork #2 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while True:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """
        raise NotImplementedError


pidpath = os.path.join(os.path.expanduser('~'), '.procs')
dbfile = os.path.join(os.path.expanduser('~'), '.knivesout.db')
_db = osdb(dbfile)
logger = get_logger()


class _ProgramState(object):
    init = 'init'
    running = 'running'
    restart = 'restart'
    stopped = 'stopped'
    error = 'error'
    deleted = 'deleted'


class Config(BaseModel):
    program: str
    directory: str
    command: str
    stdout_file: Optional[str] = '/tmp/stdout.txt'
    stderr_file: Optional[str] = '/tmp/stderr.txt'
    max_restart: Optional[int] = 3
    cur_restart: Optional[int] = 0
    cur_state: Optional[str] = ''
    next_state: Optional[str] = ''
    start_time: Optional[str] = pd.Timestamp.now().strftime(
        '%Y-%m-%d %H:%M:%S')
    restart_period: Optional[int] = sys.maxsize

    def __str__(self):
        return str(self.dict())

    def __eq__(self, other):
        return self.program == other.program

    def __hash__(self):
        return hash(self.program)


def parse_config_from_file(config_file: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    try:
        js = cf.js(config_file)
        return Config(**js)
    except json.decoder.JSONDecodeError as e:
        logger.warning("json decode error: {}".format(e))
        js = ast.literal_eval(cf.io.reads(config_file))
        return Config(**js)
    except Exception as e:
        logger.warning(e)
        return None


def parse_config_from_string(config_string: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    import ast
    try:
        js = ast.literal_eval(config_string)
        return Config(**js)
    except Exception as e:
        cf.error({
            'msg': 'parse_config_from_string error',
            'config_string': config_string,
            'error': str(e)
        })
        return None


class ConfigManager(object):

    @staticmethod
    def get_by_program(program: str) -> Config:
        return next((c for c in ConfigManager.load() if c.program == program),
                    None)

    @staticmethod
    def load() -> List[Config]:
        configs = _db.get('configs') or '[]'
        configs = [Config(**c) for c in ast.literal_eval(configs)]
        return list(set(configs))

    @staticmethod
    def add(config: Config):
        configs = ConfigManager.load()
        configs = [c for c in configs if c != config]
        configs.append(config)
        ConfigManager.save(configs)

    @staticmethod
    def _kill_by_pid(pid: int):
        try:
            os.kill(pid, SIGTERM)
        except Exception as e:
            logger.warning(e)

    @staticmethod
    def _kill_by_command(config: Config):
        pids = os.popen(
            f"ps -ef | grep '{config.command}' | grep -v grep | awk '{{print $2}}'"
        ).read().split()
        for pid in pids:
            ConfigManager._kill_by_pid(int(pid))

    @staticmethod
    def delete_by_program_name(name: str):
        configs = ConfigManager.load()
        configs_new = []
        for c in configs:
            if c.program == name:
                ConfigManager._kill_by_command(c)
            else:
                configs_new.append(c)
        ConfigManager.save(configs_new)

    @staticmethod
    def stop_by_program_name(name: str):
        configs = ConfigManager.load()
        configs_new = []
        command = ''
        for c in configs:
            if c.program == name:
                c.next_state = _ProgramState.stopped
                c.cur_state = _ProgramState.running  # Give control to RunningSwitcher
                c.start_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
                command = c.command
            configs_new.append(c)
        ConfigManager.save(configs_new)
        return command

    @staticmethod
    def save(configs: List[Config]):
        configs = list(set(configs))
        configs = [c.dict() for c in configs]
        _db.set('configs', configs)


class AbstractStateSwitcher(ABC):

    def _update_config(self, config: Config):
        ConfigManager.add(config)

    @abstractmethod
    def is_match(self) -> bool:
        ...

    @abstractmethod
    async def _switch(self):
        ...

    async def switch(self, config: Config):
        self.config = config
        if not self.is_match():
            return
        await self._switch()

    async def get_pids(self, config: Config) -> List[str]:
        pids = os.popen(
            f"ps -ef | grep '{config.command}' | grep -v grep | awk '{{print $2}}'"
        ).read().split()
        return pids

    def reset_states(self, config: Config, cur_state: str,
                     next_state: str) -> Config:
        config.cur_state = cur_state
        config.next_state = next_state
        return config

    async def is_running(self, config: Config):
        pids = await self.get_pids(config)
        return len(pids) > 0

    async def stop_execute(self, config: Config) -> None:
        pids = await self.get_pids(config)
        logger.info(f"stop running [{config.command}], pids {pids}")

        config = self.reset_states(config, _ProgramState.stopped,
                                   _ProgramState.stopped)
        self._update_config(config)

        for pid in pids:
            os.system(f"kill -9 {pid}")

    async def restart_execute(self, config: Config):
        """stop and then start program"""
        pids = await self.get_pids(config)
        logger.info(f"restarting [{config.command}], pids {pids}")
        for pid in pids:
            os.system(f"kill -9 {pid}")

        config.cur_state = _ProgramState.init
        config.next_state = _ProgramState.running
        config.cur_restart = 0
        self._update_config(config)


class InitSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.init and self.config.next_state == _ProgramState.running

    async def _switch(self):
        await self.start_execute(self.config)

    def check_log_file_permission(self, config: Config):
        if not os.path.exists(config.stdout_file):
            return True

        if not os.path.exists(config.stderr_file):
            return True

        if not os.access(config.stdout_file, os.W_OK):
            cf.error(f"stdout_file {config.stdout_file} is not writable")
            return False

        if not os.access(config.stderr_file, os.W_OK):
            cf.error(f"stderr_file {config.stderr_file} is not writable")
            return False
        return True

    def to_error_state(self, config: Config):
        config.cur_state = _ProgramState.error
        config.next_state = _ProgramState.error
        self._update_config(config)

    def to_running_state(self, config: Config):
        config.cur_state = _ProgramState.running
        self._update_config(config)

    async def start_execute(self, config: Config):
        if config.cur_restart >= config.max_restart:
            cf.error(
                f"restart [{config.command}] reached retry limit {config.max_restart}"
            )
            self.config.cur_state = _ProgramState.error
            self.config.next_state = _ProgramState.error
            self._update_config(self.config)

        else:
            logger.info(f'start config: {config}')
            if not self.check_log_file_permission(config):
                self.to_error_state(config)
                return
            else:
                self.to_running_state(config)

            cmd = f"{config.command} 1>> {config.stdout_file} 2>> {config.stderr_file}"
            logger.info(f"Start running [{config.command}]")
            is_running = await self.is_running(config)

            if is_running:
                logger.info({'msg': 'already running', 'config': config})
            else:
                self.config.start_time = pd.Timestamp.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
                self._update_config(self.config)

                os.chdir(config.directory)
                proc = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE)
                stdout, stderr = await proc.communicate()

                # Failed to start or been terminated
                msg = {
                    'stdout': stdout,
                    'stderr': stderr,
                    'return code': proc.returncode
                }
                logger.info(msg)
                if int(proc.returncode) not in (0, ):
                    msg = (
                        f"[{config.command}] is either terminated or failed to start, "
                        "return code: {proc.returncode}")
                    logger.warning(msg)

                config = ConfigManager.get_by_program(config.program)
                config.cur_restart += 1
                self._update_config(config)


class RunningSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.running

    def running_time(self) -> float:
        uptime = pd.Timestamp.now() - pd.Timestamp(self.config.start_time)
        return uptime.total_seconds()

    async def restart_by_period(self, config: Config):
        if self.running_time() > config.restart_period:
            await self.restart_execute(config)

    async def running_execute_helper(self, config: Config):
        is_running = await self.is_running(config)
        if not is_running:  # program maybe dead and stuck on running state
            self.config.cur_state = _ProgramState.init
            self.config.next_state = _ProgramState.running
            self._update_config(config)
        await self.restart_by_period(config)

    async def _switch(self):
        stratergies = {
            _ProgramState.stopped: self.stop_execute,
            _ProgramState.restart: self.restart_execute,
            _ProgramState.running: self.running_execute_helper,
        }
        await stratergies[self.config.next_state](self.config)


class StopSwitcher(AbstractStateSwitcher):

    def is_match(self) -> bool:
        return self.config.cur_state == _ProgramState.stopped

    def restart(self, config: Config) -> None:
        config.cur_state = _ProgramState.init
        config.next_state = _ProgramState.running
        self._update_config(config)

    def delete(self, config: Config) -> None:
        self.stop_execute(config)

    async def _switch(self):
        if self.config.next_state in (_ProgramState.init,
                                      _ProgramState.running):
            self.restart(self.config)


class Context(object):
    _SWITCHERS = [RunningSwitcher(), InitSwitcher(), StopSwitcher()]

    @staticmethod
    async def run():
        configs = ConfigManager.load()
        for config in configs:
            for switcher in Context._SWITCHERS:
                asyncio.create_task(switcher.switch(config))


class ResetStdFiles(object):

    def __init__(self, file_size_limit: int = 500000) -> None:
        self.file_size_limit = file_size_limit

    async def get_file_size(self, filepath: str) -> int:

        def filesize(filepath: str) -> int:
            return cf.shell('du -s {} | cut -f1'.format(filepath))

        return int(await async_render(filesize, filepath))

    async def rename_file(self, filepath):
        return await async_render(
            cf.shell, "mv {} {}".format(filepath, filepath + '.bak'))

    async def run(self):
        for f in ['/tmp/stdout.txt', '/tmp/stderr.txt']:
            filesize = await self.get_file_size(f)
            if filesize > self.file_size_limit:
                await self.rename_file(f)


class AbstractExecutor(ABC):

    @abstractmethod
    def serve(self, *args, **kwargs):
        pass

    @abstractmethod
    def is_match(self) -> bool:
        pass

    def exec(self, *args, **kwargs):
        if self.is_match():
            self.serve(*args, **kwargs)


class DaemonRunner(AbstractExecutor):

    async def _loop(self):
        reset_std = ResetStdFiles()
        while True:
            await asyncio.sleep(1)
            await Context.run()
            await reset_std.run()

    def serve(self, *args, **kwargs):
        asyncio.run(self._loop())

    def is_match(self):
        return True


class KnivesoutDaemon(Daemon):

    def run(self):
        DaemonRunner().exec()
        logger.info('exit knivesout daemon')


def knivesd():
    if not os.path.exists(pidpath):
        os.makedirs(pidpath)
    pidfile = os.path.join(pidpath, 'knivesd.pid')
    fire.Fire(KnivesoutDaemon(pidfile))


class KnivesCli(object):
    """Terminal cli powered by fire."""

    def _check_daemon_status(self) -> None:
        """Check daemon status."""
        logger.info('Checking daemon status...')
        status = cf.shell('systemctl status knivesd')
        if not 'active (running)' in status:
            logger.warning('knivesd is not running')

    def _identify_config(self, proc_or_file: str) -> Config:
        """Find config by proc or file name

        Args:
            proc_or_file (str): proc or file name

        Returns:
            _type_: Config
        """

        configs = ConfigManager.load()
        config = next((c for c in configs if c.program == proc_or_file), None)
        file_exist = os.path.exists(proc_or_file) and os.path.isfile(
            proc_or_file)

        if file_exist:
            c_file = parse_config_from_file(proc_or_file)

            config = next((c for c in configs if c.program == c_file.program),
                          None)

            # Tasks with same program name is forbidden
            if config:
                logger.info(f"Program [{config.program}] already exists")
            config = c_file

        if not config:
            logger.warning(f"Program [{proc_or_file}] not found")
            sys.exit(1)
        return config

    def init(self, name: str, command: str, directory: str = None):
        """Init a program, usage: knives init --name=xxx --command=xxx --directory=xxx

        Args:
            name (str): program name
            command (str): command to run
            directory (str, optional): directory to run. Defaults to None.
        """
        c = {
            'program': name,
            'command': command,
            'directory': directory or cf.shell('pwd')
        }
        filepath = '/data/knivesd/{}.json'.format(name)
        try:
            cf.js.write(c, filepath)
        except FileNotFoundError:
            filepath = os.path.join(os.getcwd(), '{}.json'.format(name))
            cf.js.write(c, filepath)
        self.start(filepath)

    def start(self, proc_or_file: str):
        """Start a program."""
        config = self._identify_config(proc_or_file)

        if config:
            config.cur_state = _ProgramState.init
            config.next_state = _ProgramState.running
            c = next((_ for _ in ConfigManager.load() if _ == config), None)
            if c:
                config.start_time = c.start_time

            config.cur_restart = 0
            ConfigManager.add(config)
            logger.info(f"[{config.command}] started")
        else:
            logger.info(f"config not found: {proc_or_file}")

    def stop(self, proc_or_file: str):
        """Stop a program."""
        config = self._identify_config(proc_or_file)
        program = ConfigManager.stop_by_program_name(config.program)
        logger.info(f"[{program}] stopped")

    def restart(self, proc: str):
        """Restart a program."""
        config = self._identify_config(proc)
        config.cur_state = _ProgramState.running
        config.next_state = _ProgramState.restart
        ConfigManager.add(config)
        logger.info(f"[{config.program}] restarted")

    def _get_all_configs(self, proc: str = None) -> List[Config]:
        return cf.lis(ConfigManager.load())\
            .filter(lambda c: proc is None or c.program == proc)\
            .sort(lambda c: (c.cur_state, c.program)).data

    def _get_printable_config(self, configs: List[Config]) -> str:

        def _uptime_str(c: Config):
            uptime = pd.Timestamp.now() - pd.Timestamp(c.start_time)
            seconds = uptime.total_seconds()
            return cf.fp.readable_time(seconds)

        def _format(data: List[Tuple]) -> str:
            return ' | '.join([f'{d[1]:<{d[0]}}' for d in data])

        def _printable_text(c: Config) -> str:
            state = c.cur_state
            mapping = {
                _ProgramState.running: cf.fp.green,
                _ProgramState.error: cf.fp.red,
                _ProgramState.stopped: cf.fp.cyan,
                _ProgramState.init: cf.fp.cyan
            }
            state = mapping.get(state, cf.fp.cyan)(state.upper())
            return _format([
                (7, state),
                (13, c.program),
                (15, _uptime_str(c)),
                (30, c.command),
            ])

        contents = [(7, 'state'), (13, 'proc_alias'), (15, 'uptime'),
                    (30, 'command')]
        text = _format(contents)
        texts = [text, '-' * 66]

        cf.lis(configs).map(_printable_text).each(texts.append)
        return '\n'.join(texts)

    def status(self, proc: str = None):
        """Show status of a program."""
        print(self._get_printable_config(self._get_all_configs(proc)))

    def st(self, proc: str = None):
        """Alias of status"""
        self.status(proc)

    def delete(self, proc: str):
        """Delete a program."""
        ConfigManager.delete_by_program_name(proc)
        logger.info(f"[{proc}] deleted")

    def configs(self, proc: str = None):
        """Show configs of a program."""
        configs = self._get_all_configs(proc)
        for config in configs:
            pprint.pprint(config.dict())

    def cs(self, proc: str = None):
        """Show configs of a program."""
        self.configs(proc)


def knivescli():
    fire.Fire(KnivesCli)
