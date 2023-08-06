# -*- coding: utf-8 -*-
# @Author  : Smawe
# @Time    : 2023/1/17 19:11
# @File    : setup.py
# @Software: PyCharm

from setuptools import find_packages, setup


NAME = 'tools_smawe'
DESCRIPTION = 'small tool'
EMAIL = '1281722462@qq.com'
AUTHOR = 'Samwe'
REQUIRES_PYTHON = '>=3.5.0'
REQUIRED = ['lxml']

about = {"__version__": "0.0.5"}

long_description = """    
    对目录中的文件进行重命名
    第某某章必须在10万章以下
    列如:
        第一百章.txt -> 第100章.txt
        """


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
