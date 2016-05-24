# -*- encoding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

setup(
    name='metu-cafeteria-menu',
    version='0.0.5',
    packages=['metu_cafeteria_menu'],
    description="A utility for fetching Middle East Technical University's cafeteria menu.",
    test_suite='tests',
    keywords=['metu', 'cafeteria', 'menu'],
    url='https://github.com/th0th/metu-cafeteria-menu',
    download_url='https://github.com/th0th/metu-cafeteria-menu/tarball/0.0.5',
    author=u'Gökhan Sarı',
    author_email='me@th0th.me',
    license='MIT',
    install_requires=[
        'beautifulsoup4==4.4.1',
    ],
    zip_safe=False,
)
