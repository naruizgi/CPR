#!/usr/bin/env python
import os
from numpy.distutils.core import setup, Extension

setup(
    name='hidrocpr',
    version='0.0.1',
    author='Hidro SIATA',
    author_email='hidrosiata@gmail.com',    
    packages=['cpr'],
    package_data={'cpr':['ensayo.py']},
    url='https://github.com/SIATAhidro/CPR.git',
    license='LICENSE.txt',
    description='Consultas-Plots y Reportes',
    long_description=open('README.md').read(),
    install_requires=[ ],
    )
