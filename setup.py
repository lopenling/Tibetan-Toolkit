# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

root = path.abspath(path.dirname(__file__))

with open(path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(root, 'LICENSE.txt'), encoding='utf-8') as f:
    license = f.read()

with open(path.join(root, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='Bokit',
    version=version,
    description='Bokit is a Python API that exposes commonly used tools for various Tibetan language workflows.',
    long_description=long_description,
    url='https://github.com/lopenling/bokit',
    author='Mikko Kotila',
    author_email='mailme@mikkokotila.com',
    license=license,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='tibetan etl tools',
    packages=find_packages(),
    extras_require={
        '': ['pytest'],
    },
    package_data={
        '': ['VERSION.txt', 'LICENSE.txt']
    },
)