import setuptools
from setuptools import setup, find_packages



with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ExeLib",
    version = "1.0.1",
    author = "Cactochan",
    packages=find_packages('src'),
    package_dir={'': 'src'},    
description = "An Alt To exec()..!!",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mastercodermerwin/ExeLib",
    project_urls = {
        "Bug Tracker": "https://github.com/mastercodermerwin/ExeLib/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
