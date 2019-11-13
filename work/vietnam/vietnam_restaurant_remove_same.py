#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 15:57
# @Author  : yangmingming
# @Site    :
# @File    : vietnam_middle_school.py
# @Software: PyCharm
folder = r"C:\Users\Administrator\Desktop"
with open(folder + r'\food_name.txt', 'r', encoding='utf8') as older_f:
    with open(folder + r'\restaurant_name.txt', 'w', encoding='utf8') as new_f:
        food_name = older_f.readlines()
        restaurtant_name = list(set(food_name))
        new_f.write(''.join(restaurtant_name))