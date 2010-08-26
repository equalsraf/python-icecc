#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
icecc - some handy tools to handle icecc schedulers
"""

from distutils.core import setup


setup(
    name = 'python-icecc',
    version = '0.1',
    description = 'icecream support tools',

    author = 'Rui Ferreira',
    author_email = 'raf.unix@gmail.com',
    license = 'BSD',
    classifiers = [
            "Programming Language :: Python",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: BSD License",
	    ],

    long_description = """
    Python support module for icecream
    ----------------------------------

    A python module with some usefull snippets to aid
    in using the icecream distributed compiler. Currently
    features:

    - A control module for remote management of icecc
      schedulers(over telnet).
    - Utility control scripts to issue commands and retrieve
      values from the scheduler

    """,

    packages = ['icecc'],
    scripts = ['scripts/icecc_control', 'scripts/icecc_value'],

)
