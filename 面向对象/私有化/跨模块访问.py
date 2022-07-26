#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：跨模块访问.py
@Author  ：WL
@Date    ：2022/7/26 17:42 
@Describe: 跨模块访问
"""
# from 公有属性访问权限 import *
# print("from导入方式访问全局公有属性：", name)

import 公有属性访问权限
print("import方式访问全局公有属性：", 公有属性访问权限.name)
