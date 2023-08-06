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
    name='result4utility',
    packages=['result4utility'],
    version='0.1.1',
    description='Result For Utility Tools',
    author='Luigelo Davila Vilchez',
    author_email='luigelo@ldvloper.com',
    url='https://github.com/luigi-dv/result4utility',
    download_url='https://github.com/luigi-dv/result4utility',
    keywords=['Restful', 'Rest', 'Util', 'Tools'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
