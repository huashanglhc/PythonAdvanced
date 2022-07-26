#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：property优化只读属性方案一.py
@Author  ：WL
@Date    ：2022/7/26 20:07 
@Describe: property

property作用：
    1. @property：可以向访问属性一样来访问某个方法
    2. property作用：将一些"属性的操作方法"关联到某一个属性中

概念补充：
    经典类：没有继承（object）
    新式类：继承(object)
    python2.0：定义一个类时，默认不继承object
    python3.0: 定义一个类时，默认继承object
    建议使用新式类
"""


class Person:
    def __init__(self, money=10):
        self.__money = money

    @property
    def money(self):
        return self.__money


p = Person(50000)
print(p.money)
p.money = 1000
