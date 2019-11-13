#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 15:24
# @Author  : yangmingming
# @Site    : 
# @File    : malaysiakini.py
# @Software: PyCharm

import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.malaysiakini.com/my"

        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        response = etree.HTML(self.resp)
        urls = response.xpath('//div[@class="uk-navbar-left"]//a/@href')
        for url in urls:
            if "http" not in url:
                print('"' + "https://www.malaysiakini.com" + url + '"' + ',')

    def save(self):
        pass

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
