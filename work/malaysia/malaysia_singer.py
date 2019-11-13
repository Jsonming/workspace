#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 8:17
# @Author  : yangmingming
# @Site    : 
# @File    : singer.py
# @Software: PyCharm

import requests
import json
import re
import execjs
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://ms.wikipedia.org/wiki/Senarai_sekolah_menengah_di_Malaysia"
        url = 'https://ms.wikipedia.org/wiki/Senarai_universiti_di_Malaysia'
        url = 'https://www.doordash.com/food-delivery'
        querystring = {"list": "PLgNjz5kKawRiPXT7l3XT60v3iWogBvGP0"}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        citys = re.findall(r'var siteMapPage = "(.*?)";', self.resp)
        site_map = citys[0].encode('latin1').decode('gbk')
        # site_map_json = json.loads(site_map)
        print(site_map)

    def save(self):
        with open('C:\\Users\\Administrator\\Desktop\\city.txt', 'a', encoding='utf-8')as f:
            f.write(','.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
