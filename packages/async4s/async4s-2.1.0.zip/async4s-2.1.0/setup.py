#!/usr/bin/env python
# -*- coding: utf-8 -*-


import io
import os

from setuptools import setup, find_packages

import async4s


cwd = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


setup(
    name="async4s",
    version=async4s.__version__,
    packages=find_packages(exclude=["test*"]),
    description="This module makes it simplely to run things in async.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rocky Peng",
    author_email="rockypengchina@outlook.com",
    url="https://github.com/meanstrong/async4s",
    maintainer="Rocky Peng",
    maintainer_email="rockypengchina@outlook.com",
    platforms=["any"],
    include_package_data=True,
    license="Apache 2.0",
    classifiers=["Programming Language :: Python", "Programming Language :: Python :: 3"],
)
