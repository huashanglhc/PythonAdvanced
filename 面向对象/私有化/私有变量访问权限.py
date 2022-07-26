#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：私有变量访问权限.py
@Author  ：WL
@Date    ：2022/7/26 19:26 
@Describe: 私有变量访问权限验证


__x私有化属性：
    类内部: 可以访问
    子类内部访问： 不可
    模块内其他位置访问： 不可以
    跨模块方法：
        import形式导入：可以
        from 模块 import * 导入
            __all__属性列表中未添加，则跨模块不能访问
            __all__属性列表中添加，则跨模块能访问

私有化属性实现机制：
    名字重整：重改__x为另外一个名称，如:_类名__x
    目的：
        1. 防止外界直接访问
        2. 防止被子类同名属性覆盖
"""


class Foo:
    __x = 100

    def func(self):
        print("类内部访问私有属性：", self.__x)


class Bar(Foo):
    def test(self):
        print("子类内部访问私有属性：", self.__x)


f = Foo()
f.func()
print("类外部名字重整机制访问：", Foo._Foo__x)
# print("类外部实例访问私有属性：", f.__x)
# print("类外包类名访问私有属性：", Foo.__x)

# b = Bar()
# print("类外部子类访问私有属性：", b.test())
# print("类外部子类实例访问私有属性：", b.__x)
# print("类外部子类访问私有属性：", Bar.__x)

__all__ = ["__name"]
__name = "李白"
