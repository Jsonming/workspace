#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 16:45
# @Author  : yangmingming
# @Site    : 
# @File    : coroutine_learn.py
# @Software: PyCharm
import asyncio
import time


async def hello():
    print("hello")
    await asyncio.sleep(3)
    print("hello")


async def hello_word():
    print("hello_word")
    await asyncio.sleep(3)
    print("hello_word")


async def hello_python():
    print("hello_python")
    await asyncio.sleep(3)
    print("hello_python")


async def h():
    task = asyncio.create_task(hello())
    task2 = asyncio.create_task(hello_word())
    task3 = asyncio.create_task(hello_python())
    await task
    await task2
    await task3


asyncio.run(h())
