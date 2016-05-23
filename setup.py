# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='metu-cafeteria-menu',
    version='0.0.1',
    description="A utility for fetching Middle East Technical University's cafeteria menu.",
    keywords=['metu', 'cafeteria', 'menu'],
    url='https://github.com/th0th/metu-cafeteria-menu',
    author=u'Gökhan Sarı',
    author_email='me@th0th.me',
    license='MIT',
    install_requires=[
        'beautifulsoup4==4.4.1',
    ],
    zip_safe=False,
)
