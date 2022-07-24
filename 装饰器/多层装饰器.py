#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：多层装饰器.py
@Author  ：WL
@Date    ：2022/7/24 15:49 
@Describe: 多层装饰器
"""
from functools import wraps


def decorate1(func):
    @wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print("我是装修队1：开始刷房子图涂料...")
        print("装修队1施工完成，耗时1周...")
        return res
    return inner


def decorate2(func):
    @wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print("我是装修队2：开始铺地板，装浴室...")
        print("装修队2施工完成，耗时2周,再过3周即可拎包入住...")
        return res
    return inner


@decorate2
@decorate1
def home(address):
    print(f"我是位于{address}的毛坯房。")


if __name__ == '__main__':
    home("陕西省汉中市城固县县委对面306套房")
