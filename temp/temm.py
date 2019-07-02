#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:58
# @Author  : yangmingming
# @Site    : 
# @File    : temm.py
# @Software: PyCharm
import re
from mylib.redis_my import MyRedis

my = MyRedis()
for i in range(51579):
    url = my.r.lpop("vietnam_news_thanhnien").decode("utf8")
    if url.endswith("https://thanhnien.vnhttps"):
        print(url)
        url = url.replace("https://thanhnien.vnhttps", "https:")
    my.r.rpush("vietnam_news_thanhnien", url)