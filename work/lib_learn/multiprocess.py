#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 18:46
# @Author  : yangmingming
# @Site    : 
# @File    : multiprocess.py
# @Software: PyCharm
import multiprocessing
from multiprocessing import Process, Queue, Pipe
import os

"""
    多线程模块，适用多cpu 充分利用多核
"""

aaa = Process()
"""
    创建进程
    三种启动模式 spawn  unix和windows都可用 继承run方法的东西，慢
    fork 所有资源继承，但是多线程分叉会有问题
    forkserver 子进程是单线程的
    multiprocessing.set_start_method() 子进程启动方式

    进程之间的通信方式    Quene和Pipe
    q = Queue()
    parent_conn, child_conn = Pipe()
    
    进程也有锁的概念，保证同时只有一个进程运行
    lock = Lock()
    
    进程源码分析
    run() 工作进程要执行的地方，可以在子类中重构此方法从初始化方法获取参数
    start()启动进程
    json() 供调用的  谁掉，谁阻塞
    name() 名字
    is_alive() 是否活着
    daemon()守护进程
    pid 进程号
    exitcode进程退出码
    authkey 进程身份验证
    terminate（）终止进程
    kill 跟上面的相同
    close（）关闭进程
    三个异常ProcessError   ProcessError  ProcessError  TimeoutError¶
    
    
"""
from multiprocessing import Process, Value, Array
"""
    共享内存，值和数组
"""

from multiprocessing import Process, Manager
"""
    服务器进程 数据管理器
    服务器进程就是单独起一个进程，该进程携带整个解释器信息。可以供其他进程使用。同共享内存， 若要保证共享内存的同步性。
    他可以用于控制远程数据管理
    
"""

from multiprocessing import Pool
"""
    工作进程
    没有啥特殊的，进程池子， 省略了进程创建的步骤
"""


bbb = Queue()
"""
    消息队列
    qsize 队列长度
    empty 队列判空
    full  队列判满
    put 
    put_nowait
    get
    get_nowait
    join_thread
"""

"""
    active_children() 查看激活的子进程
    current_process()
    freeze_support()
    get_all_start_methods(）所有启动模式
    get_context(method=None)   
    get_start_method(allow_none=False)
    set_executable()
    
"""

from multiprocessing.managers import BaseManager
manager = BaseManager(address=('', 50000), authkey=b'abc')
server = manager.get_server()
server.serve_forever()

"""可以将管理器服务运行在一台机器上，然后使用客户端从其他机器上访问"""



ddd = multiprocessing.Pool()
"""
    apply 从线程池子获取线程，并应用但是是阻塞的避免使用 可以考虑使用apply_async
    apply_async ()
    map(func, iterable[, chunksize]) 内置 map() 函数（它只支持一个 可迭代 参数）的并行版本，它会阻塞直到返回结果。
    map_async(func, iterable[, chunksize[, callback[, error_callback]]]) 

    AsyncResult 异步返回的结果类，返回结果是他对象
    
"""
