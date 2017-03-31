#!/usr/bin/env python
#coding=utf-8

from setuptools import setup, find_packages


import sys
import re


if sys.version_info < (2, 6):
    sys.exit('Python 2.5 or greater is required.')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as fp:
    readme = fp.read()


setup(
    name = 'rake-workflow',
    version = '1.1.5',
    keywords = ('rake', 'paramiko','workflow','ansible'),
    description = 'devops use workflow to  Batch Management System and Production Application ',

    long_description = readme,

    license = 'Apache Licence 2.0',

    url = 'https://github.com/djshell/rake-workflow',
    author = 'wqc2008@gmail.com',
    author_email = 'wqc2008@gmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['paramiko','PyYAML','pymongo'],
)
