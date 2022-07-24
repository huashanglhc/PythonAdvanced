#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：被装饰的函数无参数.py
@Author  ：WL
@Date    ：2022/7/24 15:19 
@Describe: 无参装饰器
"""
from functools import wraps


def decorate(f):
    @wraps(f)
    def inner():
        print("开始装饰无参装饰器")
        f()
        print("无参装饰器装饰完毕")
    return inner


@decorate
def func():
    print("我是无参装饰器")


if __name__ == '__main__':
    func()
    print(func.__name__)
