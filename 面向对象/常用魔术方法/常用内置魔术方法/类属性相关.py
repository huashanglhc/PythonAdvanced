#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：类属性相关.py
@Author  ：WL
@Date    ：2022/7/26 20:34 
@Describe: 类属性相关的魔术方法

__dict__: 类的属性
__bases__: 类的所有父类构成元组
__doc__: 类的文档字符串
__name__: 类名
__module__: 类定义所在模块
"""


class Animal:
    """动物相关的类"""

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def eat(self, food):
        """动物吃食物的公共方法"""
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Dog(Animal):
    """小狗类"""
    def eat(self, food):
        print(f"小狗的名字是：{self.name}, 喜欢吃的食物是：{food}")


print(f"查看Animal类的属性字典：{Animal.__dict__}")
print(f"查看Dog类的属性字典：{Dog.__dict__}")
print(f"查看Animal类的基类信息：{Animal.__bases__}")
print(f"查看Dog类的基类信息：{Dog.__bases__}")
print(f"查看Animal类的文档信息：{Animal.__doc__}")
print(f"查看Dog类的文档信息：{Dog.__doc__}")
print(f"查看Animal类的名字：{Animal.__name__}")
print(f"查看Dog类的名字：{Dog.__name__}")
print(f"查看Animal类定义所在模块：{Animal.__module__}")
print(f"查看Dog类类定义所在模块：{Dog.__module__}")
