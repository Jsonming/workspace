#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 9:43
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_moive_filtrate.py
# @Software: PyCharm
import re

s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
# a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)
# print(a)

s2 = u"我是一个人（中国人）aaa[真的]bbbb{确定}【ys】21"
s3 = s + s2
a = re.sub(u"\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]", "", s3)
print(a)
