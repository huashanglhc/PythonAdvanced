#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：orm实现进阶.py
@Author  ：WL
@Date    ：2022/7/4 21:42 
@Describe:  orm实现进阶
"""

from typing import Dict, Any


class ModelMetaclass(type):
    def __new__(mcs, name: str, base: tuple, attrs: Dict[str, Any]):
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mappings
        attrs['__table__'] = name
        return type.__new__(mcs, name, base, attrs)


class Model(metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mapping__.items():
            fields.append(k)
            args.append(getattr(self, k, None))
        # 判断字段类型，判断是否添加引号
        args_tmp = []
        for value in args:
            # 如果是int类型，则设置为str字符串，用于后续join的拼接
            if isinstance(value, int):
                args_tmp.append(str(value))
            # 如果是str类型，则增加引号
            if isinstance(value, str):
                args_tmp.append(f"""'{value}'""")

        sql = f"insert into {self.__table__} ({','.join(fields)}) values ({','.join(args_tmp)})"
        print(f"SQL: {sql}")


class User(Model):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(35)')
    email = ('email', 'varchar(30)')
    password = ('password', 'varchar(30)')


class Student(Model):
    # 定义字段映射关系
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    classroom = ('room', "varchar(30)")


if __name__ == '__main__':
    u = User(uid=1, name='李白', email='wl1548139795@163.com', password='123456')
    u.save()

    stu = Student(uid=123, name='杜甫', classroom='room1')
    stu.save()
