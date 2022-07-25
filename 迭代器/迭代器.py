#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：迭代器.py
@Author  ：WL
@Date    ：2022/7/24 16:47 
@Describe: 迭代器01

可迭代对象：列表、元组、字典和集合都是可迭代的对象，他们是可迭代容器，这些对象可以用iter()转换层迭代器
迭代器：迭代器是一种对象，该对象包含值的可计数数字。实现了迭代协议__iter__， __next__

优点：
    1. 提供了一种通用不依赖索引的迭代取值方式
    2. 惰性计算：对迭代器本身来说，同一时刻在内存中只有一个值，它可以存放无限大的数据流，可以节省内存
缺点：
    1. 取值麻烦，无法预测值的长度
    2. 不能控制取值顺序，只能取下一个值，更不能回到开始，调用是一次性的，若想重新获取值值，只能重新调用__iter__（）方法
        或iter()生成一个新的迭代器。
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
