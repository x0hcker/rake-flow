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
    name = 'rake-flow',
    version = '2.3',
    keywords = ('rake', 'paramiko','workflow','ansible'),
    description = 'devops use workflow to  Batch Management System and Production Application ',

    long_description = readme,

    license = 'Apache Licence 2.0',

    url = 'https://github.com/x0hcker/rake-flow',
    author = 'x0hcker@gmail.com',
    author_email = 'x0hcker@gmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['paramiko','PyYAML','pymongo'],
)
