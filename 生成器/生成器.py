#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：生成器.py
@Author  ：WL
@Date    ：2022/7/25 17:46 
@Describe: 生成器

生成器：这种一边循环一边计算的机制，称为生成器：generator。生成器（generator）是一种返回一个值的迭代器，每次从该迭代器取下一个值

创建生成器：
    1. 生成器表达式
    2. 生成器函数（yield）

return vs yield:
    return:遇到return就返回结果，函数调用结束返回结果
    yield: 遇到yield就返回结果，结束，下次再调用时，从上次yield离开的地方进入。相当于（return + 暂停）

向生成器发送数据：
    生成器对象.send(value):可以向生成器对象发送一个数据
    当生成器函数中执行yield时，程序会卡在yield的地方不执行，next()和send()的作用就是唤醒卡住的程序，让他继续执行。
"""


def odd():
    print("第一次...")
    res = yield 1
    print("接收send发送的值", res)
    print("第二次调用")
    yield 2
    print("第三次调用")
    yield 3


o = odd()
while 1:
    try:
        next(o)
        o.send("hello world！！！")
    except Exception:
        raise StopIteration("迭代终止...")
