#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 10:30
# @Author  : yangmingming
# @Site    : 
# @File    : world_new.py
# @Software: PyCharm
from work.temporary.temp_task_urls import task_urls

import requests
import re
import pprint
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.resp = None

    def crawl_get(self, url, headers=None):
        if not headers:
            _headers = headers
        else:
            _headers = self.headers

        response = requests.request("GET", url, headers=_headers)
        self.resp = response.text

    def crawl_post(self, url, data, headers=None):
        if not headers:
            _headers = headers
        else:
            _headers = self.headers

        response = requests.request("POST", url, data=data, headers=_headers)
        self.resp = response.text

    def parse_html(self):
        html = etree.HTML(self.resp)
        nodes = html.xpath('//*[@id="orb-modules"]/header/div[2]/div[2]/div[1]/nav/ul//a/@href')
        for node in nodes:
            if "http" not in node:
                url = '"' + "https://www.bbc.com" + node + '",'
                print(url)

    def parse_json(self):
        names = []
        response = json.loads(self.resp)
        stores = response.get("stores")
        for store in stores:
            store_name = store.get("business").get("name")
            names.append(store_name)

    def run(self):
        url = task_urls[0]
        print(url)

        self.crawl_get(url)
        self.parse_html()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
