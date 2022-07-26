#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：私有方法.py
@Author  ：WL
@Date    ：2022/7/26 20:37 
@Describe: 私有方法
"""


class Person:
    def __func(self, name="__func"):
        print(f"我是私有方法：{self}, 我的名字是：{name}")


p = Person()
# 不建议通过名字重整机制访问
# print(Person._Person__func("hello"))
print(Person.__dict__)
