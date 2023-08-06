#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zzz(1309458652@qq.com)
# Description:

from setuptools import setup, find_packages

setup(
    name = 'webz',
    version = '0.0.1',
    keywords='webz',
    long_description=open('README.md', 'r', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    description = "简单的web服务器框架，实现的是配置文件的读取和调用，内部调用web.py",
    license = 'MIT License',
    url = 'https://github.com/buildCodeZ/webz',
    author = 'Zzz',
    author_email = '1309458652@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)