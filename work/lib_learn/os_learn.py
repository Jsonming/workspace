#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 23:35
# @Author  : yangmingming
# @Site    : 
# @File    : os_learn.py
# @Software: PyCharm
import os
import sys

# print(os.name)
# print(os.environ)
# print(os.getcwd())
# floder = r"C:\Users\Administrator\Desktop\indonesia_temp"
# os.chdir(floder)

# print(os.__all__)
# print(sys.builtin_module_names)

# pwd = os.getcwd()
# to_folder = r"D:\datatang\language"
# os.chdir(to_folder)
# print(os.getcwd())

os.makedirs('./a/b/c/e/f')
# os.remove('b.txt')
# os.removedirs('./a/b/c/e/f')
# os.rename('a.txt', 'b.txt')
# with open('a.txt', 'w', encoding='utf8')as f:
#     f.write("he")

# stat = os.stat('a.txt')
# print(stat)

# print(os.sep)
# os.system('dir')

# print(os.path.abspath('a.txt'))
# print(os.path.join("root", "passwd.txt"))
print(os.environ)