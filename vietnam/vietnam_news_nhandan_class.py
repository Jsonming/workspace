#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 16:52
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_news_nhandan.py
# @Software: PyCharm
import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "http://www.nhandan.org.vn/"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)

        print(self.resp)
        html = etree.HTML(self.resp)
        names = html.xpath('//*[@id="nddt-navbar-collapse-1"]/ul[1]/li/a/@href')
        names = names[1:]
        links = ['http://www.nhandan.org.vn' + item for item in names][1:]
        print(links)
        self.save(links)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
