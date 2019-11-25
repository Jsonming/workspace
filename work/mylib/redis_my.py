#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 17:59
# @Author  : yangmingming
# @Site    : 
# @File    : redis_my.py
# @Software: PyCharm
import hashlib
import redis


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

    def get_finger(self):
        a = self.r.hkeys("fingerprint")
        print(a)


if __name__ == '__main__':
    mr = MyRedis()
    mr.get_finger()
