#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 15:56
# @Author  : yangmingming
# @Site    : 
# @File    : mysql_my.py
# @Software: PyCharm

import pymysql.cursors

LIMIT_NUMBER = 2


class MySql(object):

    def __init__(self):
        # 连mysql接数据库
        self.connect = pymysql.connect(
            # host='127.0.0.1',
            # user='root',
            # passwd='Yang_123_456',

            host='123.56.11.156',
            user='sjtUser',
            passwd='sjtUser!1234',

            db='spiderframe',
            port=3306,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def get_many(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchmany(LIMIT_NUMBER)
        while data:
            yield data
            data = self.cursor.fetchmany(LIMIT_NUMBER)


class ScrapyRedis():
    def __init__(self):
        redis_key = 'news_link'
        custom_settings = {
            'REDIS_HOST': '123.56.11.156',
            'REDIS_PORT': 6379,
            'REDIS_PARAMS': {
                'password': '',
                'db': 0
            },
        }
