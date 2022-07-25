#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：实现迭代器.py
@Author  ：WL
@Date    ：2022/7/24 16:58 
@Describe: 实现迭代器
"""


class Iter:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration("迭代终止")
        self.index -= 1
        return self.data[self.index]


if __name__ == '__main__':
    obj = Iter([1, 2, 3, 4, 5])
    for i in obj:
        print(i)
