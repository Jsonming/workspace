#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 14:08
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_word_to_redis.py
# @Software: PyCharm
from work.mylib.redis_my import MyRedis


def gen_url():
    urls = []
    with open('chinese_word.txt', 'r', encoding='utf8')as f:
        for item in f:
            url = 'https://vi.glosbe.com/zh/vi/{}'.format(item.strip())
            urls.append(url)
    return urls


def insert_db():
    urls = gen_url()
    my_redis = MyRedis()
    for url in urls:
        my_redis.insert_('vietnam_speaking_url', url)


insert_db()
