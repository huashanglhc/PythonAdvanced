#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：类.py
@Author  ：WL
@Date    ：2022/7/25 22:21 
@Describe: 初始类
"""


class Foo:
    # 类属性
    name = "李白"

    def __init__(self, data):
        # 实例属性
        self.data = data

    def func(self):
        """实例方法"""
        return self.data

    # 类方法
    @classmethod
    def get(cls, key):
        return f"{cls.name}的职业是：{key}"

    @staticmethod
    def tool(key, value):
        return {key: value}

