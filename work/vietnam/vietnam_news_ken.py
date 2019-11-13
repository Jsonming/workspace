#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 21:51
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_news_ken.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "http://kenh14.vn/"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        response = requests.request("POST", url, data=payload, headers=headers)
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
        names = html.xpath('//ul[@class="kbh-menu-list clearfix fl"]/li//a/@href')
        urls = ["http://kenh14.vn" + item for item in names if "http"not in item]
        self.save(urls)


    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\ken_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()



