#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='realms',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Realms Game',
    # GETTING-STARTED: set author name (your name):
    author='Evan Williams',
    # GETTING-STARTED: set author email (your email):
    author_email='evanw555@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='https://github.com/evanw555',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
