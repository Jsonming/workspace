#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 21:58
# @Author  : yangmingming
# @Site    : 
# @File    : temm.py
# @Software: PyCharm
import redis
import hashlib

class MyRedis(object):
    def __init__(self):
        pool = redis.ConnectionPool(host='123.56.11.156', port=6379, db=0, password='')
        self.r = redis.Redis(connection_pool=pool)

    def generate_md5(self, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()

    def hash_(self, str):
        return self.r.hset(name="fingerprint", key=str, value=1)

    def hash_exist(self, str):
        return self.r.hexists(name='fingerprint', key=str)

    def insert_(self, key, value):
        self.r.lpush(key, value)


def run():
    my = MyRedis()
    for i in range(100):
        url = my.r.lpop("hebrew_walla_link").decode("utf8")
        if "category" in url:
            print(url)
            new_url = "https://news.walla.co.il" + url
            print(new_url)
            my.r.rpush("hebrew_walla_new_link", new_url)
        else:
            my.r.rpush("hebrew_walla_link", url)


if __name__ == '__main__':
    run()
