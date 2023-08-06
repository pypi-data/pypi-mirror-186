#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
VAERS DATA DOWNLOADER
~~~~~~~~~~~~~~~~

:copyright: © 2022
:license: MIT, see LICENSE for more details.
"""

import runpy
import os
from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    """
    Utility function to read the README file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

metadata_filename = "vaers_downloader/metadata.py"
metadata = runpy.run_path(metadata_filename)

# http://pypi.python.org/pypi?:action=list_classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Healthcare Industry",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
    "License :: OSI Approved :: MIT License",
]

setup(name='vaers_downloader',
    version=metadata['__version__'],
    description='VAERS DATA DOWNLOADER',
    classifiers=classifiers,
    keywords='vaers data downloader tensorflow captcha bypass',
    url='https://github.com/McFlat/vaers-downloader',
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    license=metadata['__license__'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data={
      "vaers_downloader": ['model/*'],
    },
    zip_safe=True,
    install_requires=read("requirements.txt").split("\n"),
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/vaers-downloader'],
)