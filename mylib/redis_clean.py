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
    for i in range(10000):
        url = my.r.lpop("hebrew_walla_link").decode("utf8")

        if "category" not in url:
            my.r.rpush("hebrew_walla_link", url)
        else:
            print(url)


if __name__ == '__main__':
    run()
