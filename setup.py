#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

cwd = os.path.abspath(os.path.dirname(__file__))

readme = open(os.path.join(cwd, 'README.md')).read()
reqs = parse_requirements(os.path.join(cwd, 'requirements.txt'))

from raspisms import __version__

setup(
    name='raspisms-pyclient',
    version=__version__,
    description="Python client for RaspiSMS API",
    long_description=readme,
    author='Emmanuel Navarro',
    author_email='enavarro222@gmail.com',
    url='https://github.com/enavarro222/RaspiSMS-pyclient',
    py_modules=['raspisms'],
    entry_points = {
        'console_scripts': ['raspisms-send=raspisms:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs,
)

