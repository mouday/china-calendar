# -*- coding: utf-8 -*-

# @Date    : 2019-06-26
# @Author  : Peng Shiyu
from __future__ import print_function, unicode_literals, absolute_import, division

import glob
import io
import os

from setuptools import setup, find_packages

"""
## 本地测试
安装测试
python setup.py develop 
python setup.py develop --uninstall

卸载
pip uninstall spideradmin -y


## 打包上传
先升级打包工具
pip install --upgrade setuptools wheel twine

打包
python setup.py sdist bdist_wheel

检查
twine check dist/*

上传pypi
twine upload dist/*

命令整合
rm -rf dist build *.egg-info \
&& python setup.py sdist bdist_wheel  \
&& twine check dist/* \
&& twine upload dist/*


## 下载测试
安装测试
pip3 install -U domain-admin -i https://pypi.org/simple

打包的用的setup必须引入

参考：
https://packaging.python.org/guides/making-a-pypi-friendly-readme/

"""

# 版本号
version_file = glob.glob("*/version.py")[0]

with io.open(version_file, 'rb') as f:
    version_var = {}
    exec(f.read(), version_var)
    VERSION = version_var['VERSION']

with io.open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

with io.open("requirements/production.txt", 'r') as f:
    install_requires = f.read().split(os.sep)

setup(
    name='china-calendar',
    version=VERSION,
    description="a calendar about china",

    keywords='china,calendar,workday,holiday',
    author='Peng Shiyu',
    author_email='pengshiyuyx@gmail.com',
    license='MIT',
    url="https://github.com/mouday/china-calendar",

    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms=['any'],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        # 'Programming Language :: Python :: 3.13',
        # 'Programming Language :: Python :: 3.14',
        # 'Programming Language :: Python :: 3.15',
        # 'Programming Language :: Python :: 999.99',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires
)
