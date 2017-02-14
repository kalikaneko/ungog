#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ungog',
    version='0.0.1',
    description='ungoogleify your css',
    author='kali kaneko',
    author_email='kali@sindominio.net',
    url='https://github.com/kalikaneko/ungog/',
    #packages=find_packages('ungog'),
    packages=['ungog'],
    entry_points={
        'console_scripts': ['ungogmycss=ungog.ungog:main']},
    classifiers=[
        "Environment :: Console",
    ],
    zip_safe=False
)
