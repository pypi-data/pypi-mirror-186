#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

readme = open('README.rst').read()

def get_version():
    VERSIONFILE = os.path.join('veritas', '__init__.py')
    VSRE = r"""^__version__ = ['"]([^'"]*)['"]"""
    version_file = open(VERSIONFILE, 'rt').read()
    return re.search(VSRE, version_file, re.M).group(1)


setup(
    name="veritas",
    version=get_version(),
    description="an executable implementation of the throwaway `_`",
    long_description=readme,
    license="BSD",
    author="lonnen",
    url='https://github.com/lonnen/veritas',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
)
