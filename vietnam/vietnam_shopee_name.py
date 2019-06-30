#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 16:36
# @Author  : yangmingming
# @Site    : 
# @File    : shopee_name.py
# @Software: PyCharm
import requests
import json
import re
from lxml import etree
from urllib.parse import unquote


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://shopee.vn/api/v2/search_items/"

        querystring = json.dumps({"by": "relevancy", "keyword": "%C4%91i%E1%BB%87n%20tho%E1%BA%A1i%20gi%C3%A1%20r%E1%BA%BB",
                       "limit": "50", "newest": "0", "ord": ""})

        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        self.resp = response.text

    def parser(self):
        # req_url = unquote(self.resp)
        # category = re.findall(r'keyword=(.*?)&', req_url)[0]
        print(self.resp)
        data = json.loads(self.resp)
        items = data.get("items")
        if items:
            for item in items:
                name = item.get("name")
                if name:
                    print(name)

    def save(self):
        stores_name = self.result
        with open('name.txt', 'a', encoding='utf-8')as f:
            for store_name in stores_name:
                f.write(store_name.strip())
                f.write(',')

    def run(self):
        self.crawl()
        self.parser()
        # self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
