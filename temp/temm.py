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
while True:
    url = my.r.lpop("vietnam_news_vtv_content").decode('utf8')
    # print()
    # https = re.findall("http", url)
    # if len(https) > 1:
    #     url = url[14:]

    # if not any([item in url for item in ['jpg', 'png', 'jpeg']]):
    #     my.r.rpush("vietnam_news_vtv_content", url)
    if not url.startswith("http"):
        new_url = url.split("source_url=")[-1]
        print(new_url)
        my.r.rpush("vietnam_news_vtv_content_new", new_url)
    else:
        my.r.rpush("vietnam_news_vtv_content", url)
