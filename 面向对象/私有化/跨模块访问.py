#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：跨模块访问.py
@Author  ：WL
@Date    ：2022/7/26 17:42 
@Describe: 跨模块访问
"""
# 公有属性跨模块访问测试
# from 公有属性访问权限 import *
# print("from导入方式访问全局公有属性：", name)

# import 公有属性访问权限
# print("import方式访问全局公有属性：", 公有属性访问权限.name)

# 受保护属性跨模块访问测试
# import 受保护属性访问
# print("import方式访问受保护属性：", 受保护属性访问._name)

# from 受保护属性访问 import *
# print("import方式访问受保护属性：", _name)

# 私有属性访问
# import 私有变量访问权限
# print("import方式访问私有属性", 私有变量访问权限.__name)
from 私有变量访问权限 import *
print("import方式访问私有属性：", __name)
