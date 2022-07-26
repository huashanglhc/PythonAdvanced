#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：公有属性访问权限.py
@Author  ：WL
@Date    ：2022/7/26 15:41 
@Describe: 私有化属性

python并没有真正的私有化支持，可以使用下划线完成伪私有的效果
x（全局变量）: 公有属性
    类内部/子类内部访问：可以
    模块内其他位置访问（类外部）: 可以
    跨模块方法：
        import形式导入：可以
        from 模块 import * 导入：可以

"""


class Foo:
    x = 100

    def func(self):
        print("类内部访问公有属性：", self.x)


class Bar(Foo):
    def test(self):
        print("子类内部访问公有属性：", self.x)


f = Foo()
f.func()
print("类外部实例访问公有属性：", f.x)
print("类外包类名访问公有属性：", Foo.x)

b = Bar()
print("类外部子类实例访问公有属性：", b.x)
print("类外部子类访问公有属性：", Bar.x)

name = "李白"


