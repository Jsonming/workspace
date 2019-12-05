#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 18:01
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm


with open('phonetic.txt', 'r', encoding='utf8')as f, open('phonetic_new.txt', 'a', encoding='utf8')as o_f:
    for line in f:
        word = line.strip().split()
        word, phonetc = word[0], ''.join(word[1:])
        o_f.write(word + "\t" + phonetc + "\n")
