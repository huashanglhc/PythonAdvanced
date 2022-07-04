#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：元类创建类.py
@Author  ：WL
@Date    ：2022/7/4 16:03 
@Describe: 元类创建类
"""
from typing import Dict, Any


def upper_class(class_name: str, class_parent: type, class_attr: Dict[str, Any]):
    new_attr = {}
    for key, val in class_attr.items():
        if not key.startswith("__"):
            new_attr[key.upper()] = val
    return type(class_name, class_parent, new_attr)


class Foo(metaclass=upper_class):
    bar = "bip"


print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))

f = Foo()
print(f.BAR)
