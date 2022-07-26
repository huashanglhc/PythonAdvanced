#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：type动态创建类.py
@Author  ：WL
@Date    ：2022/7/4 15:39 
@Describe: type动态创建类

元类的作用：
    1. 拦截类的创建
    2. 修改类
    3. 返回修改后的类
    4. 动态创建类
"""


class Test:
    name = 1
    name1 = 100


def func(self):
    print("我是实例方法...")


@classmethod
def bar(cls):
    print("我是类方法...")


@staticmethod
def test():
    print("我是静态方法...")


attr_dict = {"age": 15, "sex": "男", "func": func, "bar": bar, "test": test}
MyClass = type("MyClass", (Test,), attr_dict)
print(MyClass)
print(MyClass.__dict__)
print(MyClass.__class__)
print(MyClass.__class__.__class__)
print(MyClass.__class__.__class__.__class__)
