#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 15:56
# @Author  : yangmingming
# @Site    : 
# @File    : mysql_my.py
# @Software: PyCharm

import pymysql.cursors

LIMIT_NUMBER = 100


class MySql(object):

    def __init__(self):
        # 连mysql接数据库
        self.connect = pymysql.connect(
            # host='127.0.0.1',  # 数据库地址
            host='123.56.11.156',  # 数据库地址
            port=3306,  # 数据库端口
            db='spiderframe',  # 数据库名
            user='sjtUser',  # 数据库用户名
            # passwd='123456',  # 数据库密码
            passwd='sjtUser!1234',  # 数据库密码
            charset='utf8',  # 编码方式
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
            # 指定redis数据库的连接参数
            'REDIS_HOST': '123.56.11.156',
            'REDIS_PORT': 6379,
            # 指定 redis链接密码，和使用哪一个数据库
            'REDIS_PARAMS': {
                'password': '',
                'db': 0
            },
        }
