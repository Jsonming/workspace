#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:20
# @Author  : yangmingming
# @Site    : 
# @File    : gevent_learn.py
# @Software: PyCharm
import random
import time

import gevent
import gevent.monkey
from gevent.pool import Pool
from gevent.pool import Group

gevent.monkey.patch_all()

pool = Pool(10)


def foo():
    print('Running in foo')
    gevent.sleep(3)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(10)
    print('Implicit context switch back to bar')


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0, 2) * 0.001)
    time.sleep(10)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()

# g1 = gevent.spawn(foo)
# g2 = gevent.spawn(bar)
# g3 = gevent.spawn(bar)
#
# group = Group()
# group.add(g1)
# group.add(g2)
# group.join()
# group.add(g3)
# group.join()

pool.map(task, [12, 3, 4, ])
