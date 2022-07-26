#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：受保护属性访问.py
@Author  ：WL
@Date    ：2022/7/26 17:48 
@Describe: 受保护属性访问
_x受保护的属性：
    类内部/子类内部访问：可以
    模块内其他位置访问（类外部）： 可以，不建议
    跨模块方法：
        import形式导入: 可以，不建议
        from 模块 import * 导入：
            __all__属性列表中未添加，则跨模块不能访问
            __all__属性列表中添加，则跨模块能访问
"""


class Foo:
    _x = 200

    def func(self):
        print("类内部访问受保护属性：", self._x)


class Bar(Foo):
    def test(self):
        print("子类内部访问受保护属性：", self._x)


f = Foo()
f.func()
print("类外部实例访问受保护属性：", f._x)
print("类外包类名访问受保护属性：", Foo._x)

b = Bar()
print("类外部子类实例访问受保护属性：", b._x)
print("类外部子类访问受保护属性：", Bar._x)

__all__ = ["_name"]
_name = "李白"
