#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：函数创建元类.py
@Author  ：WL
@Date    ：2022/7/4 15:34 
@Describe: 通过函数创建元类

不建议用函数动态创建类
"""


def choose_class(name: str):
    if name == "foo":
        class Foo:
            pass
        return Foo
    elif name == "bar":
        class Bar:
            pass
        return Bar
    else:
        print("输入name不合法...")


if __name__ == '__main__':
    MyClass = choose_class("foo")
    print("MyClass---------->", MyClass)
    MyClass1 = choose_class("bar")
    print("MyClass1---------->", MyClass1)
    MyClass2 = choose_class("foo1")

