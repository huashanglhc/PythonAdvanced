#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：有参装饰器.py
@Author  ：WL
@Date    ：2022/7/24 15:47 
@Describe: 有参装饰器
"""
from functools import wraps

permissions_list = {1: "高清视频", 2: "超清视频", 3: "VIP独享清晰度", 4: "送观影卷"}


def decorate(level):
    def f(func):
        @wraps(func)
        def inner(*args, **kwargs):
            permissions = permissions_list.get(level, None)
            result = func(*args, **kwargs)
            if permissions:
                print(f"用户权限{level}享受福利:{permissions}")
            return result
        return inner
    return f


@decorate(2)
def user(name):
    print("普通用户权限：360p清晰度")
    return f"i am {name}"


if __name__ == '__main__':
    user("李白")
