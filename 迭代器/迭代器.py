#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：迭代器.py
@Author  ：WL
@Date    ：2022/7/24 16:47 
@Describe: 迭代器01

可迭代对象：支持for循环的序列对象
迭代器：实现了迭代协议__iter__， __next__
"""
from collections.abc import Iterable, Iterator

if __name__ == '__main__':
    lst = [i for i in range(10)]
    s = "abc"
    s1 = 'a'
    dt = {"a": 1, "b": 2, "c": 3}
    t = (1, 3, 5, 7)
    num = 100
    print("判断列表是不是可迭代对象：", isinstance(lst, Iterable))
    print("判断列表是不是迭代器：", isinstance(lst, Iterator))
    print("判断字符串是不是可迭代对象：", isinstance(s, Iterable))
    print("判断字符串是不是迭代器：", isinstance(s, Iterator))
    print("判断单个字符是不是可迭代对象：", isinstance(s1, Iterable))
    print("判断单个字符是不是迭代器：", isinstance(s1, Iterator))
    print("判断字典是不是可迭代对象：", isinstance(dt, Iterable))
    print("判断字典是不是迭代器：", isinstance(dt, Iterator))
    print("判断元组是不是可迭代对象：", isinstance(t, Iterable))
    print("判断元组是不是迭代器：", isinstance(t, Iterator))
    print("判断数字是不是可迭代对象：", isinstance(num, Iterable))
    print("判断数字是不是迭代器：", isinstance(num, Iterator))
