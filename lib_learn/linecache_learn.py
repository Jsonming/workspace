#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 13:54
# @Author  : yangmingming
# @Site    : 
# @File    : linecache_learn.py
# @Software: PyCharm

import pyssdb

c = pyssdb.Client('123.56.11.156', 8888)

list = ['lastName', '明明', 'firstName', '杨']
c.multi_hset('person_1', *tuple(list))
c.disconnect()
