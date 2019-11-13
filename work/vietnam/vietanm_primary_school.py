#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 14:36
# @Author  : yangmingming
# @Site    : 
# @File    : vietanm_primary_school.py
# @Software: PyCharm


import requests
import json
import re
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://hoctoantap.com/2016/04/11/danh-sach-cac-truong-tieu-hoc-tai-dia-ban-thanh-pho-ho-chi-minh.html"
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
        table = re.findall(r"theo tiếng việt có dấu:</strong></p>\n(.*)\n<hr />", self.resp, re.S)[0]
        root = etree.HTML(table)
        name = root.xpath('//table/tbody/tr/td[2]/text()')

        self.result = list(set(name))
        print(self.result)
        print(len(self.result))

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\primary_name.txt', 'r', encoding='utf-8')as f:
            # f.write('\n'.join(self.result))
            print(len(f.readlines()))
    def run(self):
        # self.crawl()
        # self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
