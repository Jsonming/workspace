#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:58
# @Author  : yangmingming
# @Site    : 
# @File    : temm.py
# @Software: PyCharm
import re
from mylib.redis_my import MyRedis


def run():
    my = MyRedis()
    urls = []
    for i in range(4558):
        url = my.r.lpop("video_bilibili_link").decode("utf8")
        new_url = url.split("?")[0]
        urls.append(new_url)
    url_list = list(set(urls))
    for n_url in url_list:
        my.r.lpush("video_bilibili_link", n_url)


if __name__ == '__main__':
    run()
