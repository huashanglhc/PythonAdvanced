#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：私有化应用场景.py
@Author  ：WL
@Date    ：2022/7/26 19:43 
@Describe: 私有化属性应用场景

私有化属性应用场景：
    1. 数据保护
    2. 数据过滤
"""


class Person:
    def __init__(self, age=1):
        self.__age = age

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError(f"输入年龄{age}不合法...")

        if age < 0 or age > 100:
            raise ValueError("不是人类，是只妖怪吧...")

        self.__age = age

    def get_age(self):
        return self.__age


p = Person()
p.set_age(900)
print(p.get_age())
