'''
Author: yuweipeng
Date: 2019-09-23 15:49:54
LastEditors: yuweipeng
LastEditTime: 2023-01-17 14:19:14
Description: file content
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lazy_testdata",
    version="1.1.9",
    author="YuWeiPeng",
    author_email="404051211@qq.com",
    description="""
    testdata include chinese personal four element and offen use datetime 测试数据包含随机生成的中国公民四要素，及常用的日期时间
    根据swagger文档生成规则用例
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.cnblogs.com/yicaifeitian/",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent", ]

    ,
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.24.0',
        'python-dateutil>=2.8.1',
        'SQLAlchemy>=1.3.17',
        'records>=0.5.3',
    ]
)
