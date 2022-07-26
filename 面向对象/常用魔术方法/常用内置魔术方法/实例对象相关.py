#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：实例对象相关.py
@Author  ：WL
@Date    ：2022/7/26 20:34 
@Describe: 实例属性相关

__dict__: 实例的属性
__class__: 实例对应的类
"""


class Person:
    """人类"""
    def __init__(self, name):
        self.name = name

    def func(self):
        """获取用户姓名"""
        return self.name

    @staticmethod
    def tools(*args, **kwargs):
        """参数校验工具"""
        print(f"{args}参数校验，{kwargs}参数校验")


p = Person("李白")
print(p.__dict__)
print(p.__class__)
