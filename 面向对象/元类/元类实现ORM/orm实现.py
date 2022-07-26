#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：orm实现.py
@Author  ：WL
@Date    ：2022/7/4 17:30 
@Describe: 元类实现orm元类

ORM: object relational Mapping，即对象-关系映射，简称ORM。

创建一个实例对象，用创建它的类名当作数据表名，用创建它的类属性对应数据表的字段，当这个实例对象操作时，能够对应MySQL语句。

目的： 操作模型对象向操作数据库一样

u = User(uid=1, name="李白", age=18)
u.save

insert into User(uid, name, age) values(1, '李白', 18);

ORM源码思路：
    1. 实例化模型类的时候，完成模型类名和数据库表名一致
    2. 实例化模型类的时候将模型类的类属性，封装到__mapping__属性中
    3. 模型类对象.save()方法的时候，实现插入sql语句转换过程
"""
from typing import Dict, Any


class ModelMetaclass:
    def __new__(cls, name: str, base: tuple, attrs: Dict[str, Any]):
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mappings
        attrs['__table__'] = name.lower()
        print("attrs-------->", attrs)
        return type(name, base, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(35)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(k)
            args.append(getattr(self, k, None))

        sql = f"""insert into {self.__table__} ({",".join(fields)}) values ({','.join([str(arg) for arg in args])})"""
        print(f"SQL: {sql}")


if __name__ == '__main__':
    u = User(uid=1, name='李白', email='wl1548139795@163.com', password='123456')
    u.save()
