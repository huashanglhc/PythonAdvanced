#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：只读属性.py
@Author  ：WL
@Date    ：2022/7/26 19:54 
@Describe: 只读属性

只读属性：一个属性（一般指实例属性），只能读取，不能写入

应用场景：有些属性，只限在内部根据不同场景进行修改，而对外界来说，不能修改，只能读取
比如：电脑网速属性，网络状态属性

实现只读属性方案一：
    1. 全部隐藏：私有化属性（既不能读也不能写）
    2. 部分公开：公开读的操作

方式一存在弊端：
    1. 不能直接通过p.money向访问属性一样访问只读属性
    2. p.money = 8000依然可以赋值成功
"""


class Person:
    def __init__(self, money=10):
        self.__money = money

    def get_money(self):
        return self.__money


p = Person(50000)
print(p.get_money())
