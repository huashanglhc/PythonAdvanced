#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：被装饰的函数带参数.py
@Author  ：WL
@Date    ：2022/7/24 15:27 
@Describe: 有参装饰器
"""
import time
from functools import wraps


def decorate(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}一共耗时：{end - start} s")
        return result
    return inner


@decorate
def binary_search(li: list, num: int) -> int:
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] < num:
            left = mid + 1
        elif li[mid] > num:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    target = 555
    lst = [i for i in range(50000000)]
    res = binary_search(lst, target)
    print(f"要查找的元素{target}在列表中的位置：{res}")
