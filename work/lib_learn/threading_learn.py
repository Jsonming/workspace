#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 14:43
# @Author  : yangmingming
# @Site    : 
# @File    : threading_learn.py
# @Software: PyCharm
import threading
from threading import Thread

print(threading.active_count())  # 获取当前存活的线程，没有创建线程的时候是一个主线程
print(threading.current_thread())  # 获取当前线程，就是创建线程的变量，如果不是有threading 创建的线程，则使mainthreading主线程
print(threading.get_ident())  # 获取线程id ，线程id没有实际意义。仅仅是表示线程之间的不同
print(threading.enumerate())  # 以列表的形式，返回所有线程线程遍历
print(threading.main_thread())  # 获取主线程
print(threading.TIMEOUT_MAX)  # 属性线程中允许阻塞的最大值
# 还有三个函数不能打印，
# settrace()跟踪每个线程，方便报错，在线程run()方法运行前面运行，接收参数fun()
# setprofile 线程预处理函数，在调用run运行前，运行函数fun
# stack_size 为线程创建堆栈，堆栈用于存储变量，函数数据的大小 默认32k

"""
以下是python 的线程的各个类
python 的类是基于java的线程设计模式设计的。但是Python对其作了修改
1.在Java里面，锁和条件变量是每个对象的基础特性，而在Python里面，这些被独立成了单独的对象。
2.Python 的 Thread 类只是 Java 的 Thread 类的一个子集
    a.目前还没有优先级，没有线程组
    b.线程还不能被销毁、停止、暂停、恢复或中断
    c. Java 的 Thread 类的静态方法在实现时会映射为模块级函数
"""

# 线程本地数据，即为线程创建的本地数据，本地数据仅为本线程使用。所以不同的线程使用不同的值
mydata = threading.local()
mydata.x = 1

# 创建一个线程
aaa = Thread()
"""
接收参数 group 为了日后扩展 ThreadGroup
target 是用于 run() 方法调用的可调用对象
name 是线程名称。默认情况下，由 "Thread-N" 格式构成一个唯一的名称
args 是用于调用目标函数的参数元组
kwargs 是用于调用目标函数的关键字参数字典。
如果 daemon 不是 None

方法：
    start()线程开始，修改线程状态信息
    run() 线程执行函数
    json() 共其他线程调用的的函数，知道被调用者执行完毕才能执行调用者信息
    name 属性和方法 线程的名字
    getName() 获取线程名称
    setName() 设置线程名称
    ident 线程id
    is_alive()是否存活
    daemon是否设置为守护线程在线程启动前设定。设置守护线程后直至其他非守护进程完成后才推出，主线程不是守护线程。
    
    多线程生成和执行的时候Python采用是轮询
"""

bbb = threading.Lock()
"""
    原始锁，直接调用的_thread模块中的分配锁
    锁对象，用于锁资源例如，变量（列表，字典），数据库链接，文件
    第一步，先获取锁，第二步执行操作  第三步释放锁
    acquire()获取锁
    release()释放锁
    blocking参数 阻塞锁和非阻塞锁   阻塞锁，运行到获取锁将资源锁死直到释放锁，非阻塞锁，是执行到获取锁，
    他会返回是否拿到锁（True or False）无论拿到没有拿到锁并不影响执行。当然，可以在代码中控制没有拿到锁的情况
    
    需要注意的是，释放锁的函数可以在任意线程中调用。意味着在a 线程中加锁可以在b线程中解锁，这种情况是不安全的，
    如果其他线程想获取锁。即使是阻塞锁，也可以通过先解锁再获取锁的操作，获取到锁
    
"""

ccc = threading.RLock()
"""
    递归调用锁  
    递归调用锁可以多次调用，当没有线程获取锁的时候，所有线程都可以获取锁，一旦有线程获取锁，只有等到该线程释放锁
    其他线程才能获取锁，假如a线程获取锁，a线程可以再一次获取锁，同时，锁的释放也是成对释放的就像是左右的括号一样。
    直到最外层的锁释放，其他线程才能获取到锁。
    
"""

ddd = threading.Condition()
"""
    条件对象
    条件对象理解：条件对象是结合锁使用的，锁的就是条件对象本身，生产者一个线程达到一定条件后，notify()给主线程发一个通知
    wait() 当跟在通知后面的时候表示等待，释放锁，  当等待被唤醒的时候是获得锁    最后程序运行结束release()释放锁
    
    当生产者释放信号后，消费者可以获取锁，执行要执行的语句，然后release释放锁，如果是达到某个条件要通知着 notify()  然后
    消费者线程进入到等待状态，生产者进入到进入到等待，一直到消费者线程自己退出
    wait_for（）等待可以传入条件
    notify_all（）唤醒所有等待的线程

"""

eee = threading.Semaphore()

"""
    一个计数器
"""

fff = threading.BoundedSemaphore()
"""
    固定上限的计数器，用于保护资源
"""

ggg = threading.Event()
"""
    线程间通信的最简单的机制，一个线程发信号，其他线程等待信号
    
"""
hhh = threading.Timer()
"""
    定时器定时执行
"""
iii = threading.Barrier()

# 到这里官方提供的threading模块 已经学习完毕。但是没有提供线程池，可以通过队列 + 线程实现
# 以下是第三方包提供的线程池，pip install threadpool

import threadpool

jjj = threadpool.ThreadPool()
"""
    创建线程池，  源码中显示它也是用队列做的
    参数创建线程池大小
"""

kkk = threadpool.makeRequests()
"""
    创建要在线程中执行的线程的请求对象
"""

lll = threadpool.WorkRequest()
"""
    工作线程，上面那个makeRequests就是调用它实现的
"""
mmm = threadpool.WorkerThread()
"""
    对threading 模块进行封装，线程池中的线程就是调用这个线程，使用的不是原始threading实现的
    上面那个threadpool.ThreadPool 是对队列进行封装把队列变成池子，池子里面的线程是调用的这个函数
"""