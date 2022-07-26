#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：静态方法使用场景.py
@Author  ：WL
@Date    ：2022/7/26 15:05 
@Describe: 静态方法使用场景
静态方法应用场景：
    1. 参数校验（检查合法性）：定义一个三角形类，可以利用静态方法监狱传入的三条边是否可以构成静态方法
    2. 静态方法就是某个类专用的工具函数。
"""
from math import sqrt


class Triangular:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        s = sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
        return s

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b


if __name__ == '__main__':
    a, b, c = 4, 1, 6
    # 静态方法和类方法都通过类方法来调用
    if Triangular.is_valid(a, b, c):
        t = Triangular(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print("无法构成三角型...")
