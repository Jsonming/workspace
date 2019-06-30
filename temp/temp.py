#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 15:45
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import urllib.parse, pyssdb, hashlib, redis
from .items import ZhihuseedsItem, ZhihuItem


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


class MongodbPipeline(object):
    def __init__(self):
        # 创建数据库连接
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=4)
        self.c = redis.Redis(connection_pool=pool)
        self.client = MongoClient("127.0.0.1:27017")
        # self.client = MongoClient("mongodb://xhql:" + urllib.parse.quote_plus("xhql_190228_snv738J72*fjVNv8220aiVK9V820@_")+"@127.0.0.1:27017/webpage")

    def process_item(self, item, spider):
        # 将数据写入数据库
        if isinstance(item, ZhihuItem):
            print('将数据写入数据库')
            # print(item)
            # item_label={}
            # item_label['id']=item['id']
            # item_label['content']=item['label_list']
            # item_label['source']='zhihu'
            # item_label['state']=0
            # item={'id': 'b7ff60fbd406805d06d5a7febc2814f2', 'title': '田村'}
            # self.client.webpage.label.update({'id': item['id']}, item_label, True)

            self.client.webpage.zhihu_details.update({'segment_id': item['segment_id']}, item, True)
            # return item
        if isinstance(item, ZhihuseedsItem):
            print('种子', item)
            list1 = item['url']
            for k in list1:
                url_hash = self.md5_(k)
                sta = self.hash_exist(url_hash)
                # sta1=sta.decode('utf-8')
                if sta == False:
                    print('url', k)
                    self.c.lpush('zhihu_seeds', k)
                    self.hash_(url_hash)

    def md5_(self, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()

    def hash_(self, str):
        return self.c.hset("zhihu_fingerprint", str, 1)

    def hash_exist(self, str):
        return self.c.hexists('zhihu_fingerprint', str)
