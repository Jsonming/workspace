#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 14:03
# @Author  : yangmingming
# @Site    : 
# @File    : korean_restaurant.py
# @Software: PyCharm


import requests
import re
import json
import chardet
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "http://month.foodbank.co.kr/section/restaurant.php?section=002&page={}".format(off_number)
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
        self.resp = response.content.decode("CP949")
        # print(chardet.detect(self.resp))

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)
        # self.result.extend(names)

        html = etree.HTML(self.resp)
        name = html.xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/table[3]/tbody/tr[3]/td/table[1]/tbody/tr/td[2]/p[1]/a/b/text()')
        # name = html.xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/table[3]/tbody/tr[3]/td/table[1]/tbody/tr/td[1]/p[1]/a/b/text()')
        self.save(name)
        print(name)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\restaurant_name_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        for i in range(40, 76):
            print(i)
            self.crawl(i)
            self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
