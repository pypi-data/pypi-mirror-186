#!/usr/bin/python3

# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='onepassword2',
    version='0.9',
    description='A python wrapper for onepassword cli version 2',
    long_description=long_description,
    long_description_content_type="text/markdown",      
    url='https://github.com/krezreb/onepassword2',
    author='krezreb',
    author_email='josephbeeson@gmail.com',
    license='MIT',
    packages=["."],
    zip_safe=False,
    install_requires=[
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
    entry_points = {
              'console_scripts': [
                  'op-signin=onepassword2:op_signin'              ],              
          },

    )





