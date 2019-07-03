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
for i in range(200):
    url = my.r.lpop("vietnam_news_vtv_content").decode("utf8")
    if "video"not in url:
        print(url)
        my.r.rpush("vietnam_news_vtv_content", url)
