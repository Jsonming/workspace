#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 16:45
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_app.py
# @Software: PyCharm


import requests
import re
import json
import os
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "https://thesmartlocal.com/read/mobile-apps-malaysia"
        # url = "https://www.freemalaysiatoday.com/category/leisure/2019/02/11/15-recommended-android-apps-for-downloading/"
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        print(self.resp)

        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)
        #
        html = etree.HTML(self.resp)
        names = html.xpath("//strong/text()")
        print(names)
        self.save(names[1:-1])

    def save(self, result):
        folder = r"C:\Users\Administrator\Desktop\malaya_temp"
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(r'{}\app_name.txt'.format(folder), 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
