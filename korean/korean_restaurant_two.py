#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:04
# @Author  : yangmingming
# @Site    : 
# @File    : korean_restaurant_two.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree
import time

class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        # url = "https://store.naver.com/sogum/api/businesses?query=%EB%A7%9B%EC%A7%91&pageIndex={}&start={}&display=20&deviceType=pc".format(off_number, 20*off_number+101)
        url = "https://store.naver.com/sogum/api/businesses?query=%EB%A7%9B%EC%A7%91&pageIndex={}&start={}&display=20&deviceType=pc".format(off_number, 20*(off_number-2)+61)
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""
        print(url)
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        response = json.loads(self.resp)
        stores = response.get("items")
        for store in stores:
            store_name = store.get("name")
            names.append(store_name)
        print(names)
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\restaurant_name_three.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        sum = 46415.45
        for i in range(247, 1024):
            self.crawl(i)
            self.parser()
            time.sleep(2)
        # self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
