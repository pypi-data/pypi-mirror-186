# -*- coding: utf-8 -*-
# @Author  : Smawe
# @Time    : 2023/1/17 19:11
# @File    : setup.py
# @Software: PyCharm
import os
import sys
from setuptools import find_packages, setup, Command, Distribution


NAME = 'example_package_smawe'
DESCRIPTION = 'test'
EMAIL = '1281722462@qq.com'
AUTHOR = 'Samwe'
REQUIRES_PYTHON = '>=3.5.0'
REQUIRED = ['lxml']

about = {"__version__": "0.0.5"}

long_description = "test test"


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)


if __name__ == '__main__':
    import subprocess
    subprocess.run("twine upload dist/*")
