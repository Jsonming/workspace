#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 16:50
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_news_thenhnien.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = off_number
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

        html = etree.HTML(self.resp)
        names = html.xpath('//nav[@class="site-header__nav"]/a/@href')
        names = html.xpath('//ul[@class="subnav-ctn clearfix"]/li/a/@href')
        # urls = ["https://thanhnien.vn" + item for item in names if 'https'not in item]

        for url in names:
            print(url)
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            for url in result:
                f.write(url + '\n')

    def run(self):
        a = [
            # 'https://thanhnien.vn/thoi-su/',
            # 'https://thanhnien.vn/the-gioi/',
            # 'https://thanhnien.vn/tai-chinh-kinh-doanh/',
            # 'https://thanhnien.vn/doi-song/',
            # 'https://thanhnien.vn/van-hoa/',
            # 'https://thanhnien.vn/gioi-tre/',
            # 'https://thanhnien.vn/giao-duc/',
            # 'https://thanhnien.vn/suc-khoe/',
            # 'https://thanhnien.vn/du-lich/',
            # 'https://thanhnien.vn/cong-nghe/',
            # 'https://thethao.thanhnien.vn/',
            'https://xe.thanhnien.vn/',
        ]
        for url in a:
            print('*'*300)
            self.crawl(off_number=url)
            self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()