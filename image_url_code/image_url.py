#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 16:44
# @Author  : yangmingming
# @Site    : 
# @File    : image_url.py
# @Software: PyCharm


import requests
import re
import pprint
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        # url = "http://textbookmall.mirae-n.com/asp/sub/Product_main.asp?SCode1=02&SCode2=03#Page=7&SCode1=02&SCode2=03&SCode3=&PageSize=24^P^list"
        url = 'http://textbookmall.mirae-n.com/asp/sub/Product_main.asp?SCode1=01&SCode2=01#Page=9&SCode1=01&SCode2=01&SCode3=&PageSize=24%5EP%5Elist'
        querystring = {"delivery_city_slug": "ramsey-ny-restau"
                                             "rants", "store_only": "true", "limit": "50",
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
        #
        # html = etree.HTML(self.resp)
        # names = html.xpath()
        # pprint.pprint(names)
        # self.save(self.resp)
        print(self.resp)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\2.html', 'a', encoding='utf-8')as f:
            f.write(result)

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()

'http://textbookmall.mirae-n.com/asp/sub/Product_main.asp?SCode1=02&SCode2=03#Page=11&SCode1=02&SCode2=03&SCode3=&PageSize=24^P^list'