#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：类装饰器.py
@Author  ：WL
@Date    ：2022/7/24 15:49 
@Describe: 类装饰器
"""


class Decorate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        print(f"我的职业是：程序员")


@Decorate
def bar(name):
    print(f"我是{name}...")


if __name__ == '__main__':
    bar("雷军")
