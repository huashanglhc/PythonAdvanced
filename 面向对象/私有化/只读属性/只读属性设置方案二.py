#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：只读属性设置方案二.py
@Author  ：WL
@Date    ：2022/7/26 20:19 
@Describe: 只读属性方案二

通过property设置只读属性：
    不安全：依然可以通过名字重整机制在类的外部去改变私有属性
"""


class Person:
    def __setattr__(self, key, value):
        """
        当我们通过实例.属性 = 值，给每一个实例增加一个属性，或者说，修改一个属性值的时候，都会调用这个方法
        在这个方法内部，才会真正的把这个属性，以及对应的数据，给存到__dict__字典中
        :param key:
        :param value:
        :return:
        """
        print(key, value)
        # 1. 判定key是不是我们设置的只读属性，self没有这个属性，则添加
        if not hasattr(self, "age"):
            self.__dict__[key] = value
        # 2. 有则屏蔽修改
        else:
            # self.key = value
            print("这个属性是只读属性，不允许设置...")


p = Person()
p.age = 19
print(p.__dict__)

p.age = 100
print(p.age)
print(p.__dict__)
