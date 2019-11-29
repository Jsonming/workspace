#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 11:05
# @Author  : yangmingming
# @Site    : 
# @File    : asyncio_learn.py
# @Software: PyCharm

import asyncio
import time

# 使用 main 函数的await 发起两个协程，此时代码仍然是同步的，
# 当第一个await 完成之后 才会启动第二个await 这是他们的运行就和函数是一致的

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())

import asyncio
import time


# 与上一个例子不同的是：这里启动协程 是通过启动 task 任务的方式，这个任务被认为是可等待的对象，因此它们可以并发的运行，本例将比上例节省一秒钟
async def say_after(delay, what):
    await asyncio.sleep(delay)
    # 为什么要使用这种方式来模拟等待？因为 time.sleep(delay) 不被asyncio认为是可等待对象，所以当替换为 time.sleep() 将不会出现预期的
    # time.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    # 用于创建协程任务
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # 并发启动任务 虽然并发的执行了，但在Python中 程序会等待最耗时的协程运行完毕后退出，所以这里耗时2秒
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())



"""
    新的协程的使用使用内置的异步包asyncio
    使用方式
        第一步定义协程要执行的任务，async def function_name()
        第二步创建异步执行      await asyncio.create_task(task)
                                await asyncio.gather(
                                    function_that_returns_a_future_object(),
                                    some_python_coroutine()
                                )
        第三步异步执行任务 asyncio.run()
"""
