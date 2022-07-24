#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：装饰器应用场景.py
@Author  ：WL
@Date    ：2022/7/24 16:26 
@Describe: 装饰器应用场景

装饰器应用场景：
    a. 参数检查
    b. 缓存
    c. 日志
    d. 函数耗时检测
"""
import time
import hashlib
import pickle

cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)
            print("装饰器内cache---------", cache)
            if key in cache and not is_obsolete(cache[key], duration):
                print('we got a winner')
                return cache[key]['value']
            result = function(*args, **kw)
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result

        return __memoize

    return _memoize


@memoize(2)
def complex_stuff(a, b):
    return a + b


if __name__ == '__main__':
    res = complex_stuff(400, 200)
    print(res)
    res = complex_stuff(400, 200)
    print(res)
