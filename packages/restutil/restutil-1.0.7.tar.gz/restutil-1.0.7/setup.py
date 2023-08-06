#! usr/bin/python
# -*- coding: utf-8 *-*

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

from pathlib import Path

root_dir = Path(__file__).parent
long_description = (root_dir / "README.md").read_text()

setup(
    name='restutil',
    packages=['restutil'],
    version='1.0.7',
    description='Rest Util Tools',
    author='Adonis Gonzalez Godoy',
    author_email='adions025@gmail.com',
    url='https://github.com/adions025/restutil',
    download_url='https://github.com/adions025/restutil',
    keywords=['Restful', 'Rest', 'Util', 'Tools'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
