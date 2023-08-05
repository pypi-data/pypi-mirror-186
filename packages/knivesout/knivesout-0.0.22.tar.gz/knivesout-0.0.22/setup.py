import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knivesout",
    version="0.0.22",  # Latest version .
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="ok",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/",
    packages=setuptools.find_packages(),
    package_data={setuptools.find_packages()[0]: ["bash/*"]},
    install_requires=['fire', 'pandas', 'codefast>=0.9.9', 'pydantic'],
    entry_points={
        'console_scripts': [
            'knivescli=knivesout.knivesout:knivescli',
            'ko=knivesout.knivesout:knivescli', # keep alias shorter and easier
            'knivesd=knivesout.knivesout:knivesd'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
