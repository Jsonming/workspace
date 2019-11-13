#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 14:16
# @Author  : yangmingming
# @Site    : 
# @File    : replace_word_replace.py
# @Software: PyCharm
import os


def repl(file_name):
    with open(file_name, 'r', encoding='utf8')as f:
        data = f.read().encode('utf8').decode('utf8')

    new_data = data.replace(',', '\n')
    with open(file_name, 'w', encoding='utf8')as f:
        f.write(new_data)


dir_name = 'C:\\Users\\Administrator\\Desktop\\替换词\\酒店名'
# dir_list = os.listdir(dir_name)
# for dir in dir_list:
#     dir_ = os.path.join(dir_name, dir)
#     file_list = os.listdir(dir_)
#     for file_name in file_list:
#         file_name = os.path.join(dir_, file_name)
#         repl(file_name)
#         print(file_name)
file_names = os.listdir(dir_name)
for file_name in file_names:
    file = os.path.join(dir_name, file_name)
    repl(file)