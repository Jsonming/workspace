#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 10:35
# @Author  : yangmingming
# @Site    : 
# @File    : yes24.py
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
        url = "http://www.yes24.com"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'Cookie': 'PCID=15705851714321131492806; RecentViewGoods=; RecentViewInfo=NotCookie%3DY%26Interval%3D5; __utmz=12748607.1570585274.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=12748607.1624611560.1570585274.1570585274.1570590050.2; yes24_glbola_redirect=validationcheck=true|nation_id=china; HTTP_REFERER=; WiseLogParam=Null; wcs_bt=s_1b6883469aa6:1570590663; __utmc=12748607; __utmt=1; __utmb=12748607.6.10.1570590050'
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
        print(self.resp)
        # with open('a.html', 'w', encoding='utf8')as f:
        #     f.write(self.resp)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
