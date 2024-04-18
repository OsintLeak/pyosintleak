#!/usr/bin/env python3

import io
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

ol_version = '1.0.0'

setup(
    name='pyosintleak',
    version=ol_version,
    description='pyosintleak is a library designed for utilizing the osintleak API, facilitating integration and automation of open-source intelligence operations.',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='OsintLeak',
    author_email='help@osintleak.com',
    url='https://github.com/osintleak/pyosintleak',
    download_url='https://github.com/osintleak/pyosintleak/archive/v%s.zip' % ol_version,
    zip_safe=False,
    include_package_data=True,
    package_data={'pyosintleak': ['config.json']},
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'osintleak = pyosintleak.cli:main'
        ]
    },
    keywords=['osintleak', 'osint', 'leak', 'breach', 'search', 'ol', 'pentesting'],
)
