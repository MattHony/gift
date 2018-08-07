# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/7 20:16
# @Author : '红文'
# @File : test3.py
# @Software: PyCharm
from contextlib import contextmanager


class MyResource:

    def query(self):
        print('query data')


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')


# yield 生成器
with make_myresource() as r:
    r.query()
