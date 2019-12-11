#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 11:15
# @Author  : yangmingming
# @Site    : 
# @File    : threading_demo.py
# @Software: PyCharm
from threading import Thread
import time

"""
Python中使用线程有两种方式：函数或者用类来包装线程对象。

函数式：调用thread模块中的start_new_thread()函数来产生新线程
thread.start_new_thread ( function, args[, kwargs] )
"""
global a
a = []


def aaa():
    print(1111)
    time.sleep(1)
    print(2222)
    a.append("1")


def bbb():
    print(333)
    time.sleep(1)
    print(444)
    a.append("2")


t_1 = Thread(target=aaa)
t_2 = Thread(target=bbb)

t_1.start()
t_1.join()
t_2.start()
t_2.join()

print(a)
