#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup
from thumbor_spaces import __version__
from setuptools import find_packages

setup(
    name = "thumbor_spaces",
    packages = find_packages(),
    version = __version__,
    description = "spaces addons for Thumbor",
    author = "Siddhartha Mukherjee",
    author_email = "mukherjee.siddhartha@gmail.com",
    keywords = ["thumbor", "spaces", "images", "cloud"],
    license = 'MIT',
    url = 'https://github.com/siddhartham/thumbor_spaces',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_spaces": "thumbor_spaces"},
    requires=["thumbor"],
    long_description = """\
Provides a Thumbor result storage adapter for Spaces that stores files in DigitalOcean.
"""
)