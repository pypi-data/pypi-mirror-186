#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='bigbashview',
    scripts=['bigbashview'],
    version='3.7.3',
    description='Graphical Frontends for shellscripts using HTML/JS/CSS',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='eltonff',
    author_email='eltonfabricio10@gmail.com',
    url='https://github.com/biglinux/bigbashview/tree/master/bigbashview/usr/share/bigbashview',
    install_requires=['web.py', 'PySide6', 'setproctitle'],
    license='GPLv2+',
    keywords=['big', 'bigbashview', 'biglinux', 'bash', 'webview', 'view', 'web'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
