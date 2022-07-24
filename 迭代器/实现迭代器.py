#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：实现迭代器.py
@Author  ：WL
@Date    ：2022/7/24 16:58 
@Describe: 实现迭代器
"""
from collections.abc import Iterator, Iterable


class Iter:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    # def __next__(self):
    #     pass


if __name__ == '__main__':
    print(isinstance(Iter(), Iterable))
    print(isinstance(Iter(), Iterator))
