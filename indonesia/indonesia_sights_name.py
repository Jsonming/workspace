#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 9:05
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_sights_name.py
# @Software: PyCharm
import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        # url = "https://www.tripadvisor.co.id/Attractions-g294225-Activities-Indonesia.html"
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
        name_one = html.xpath('//*[@id="taplc_attraction_coverpage_attraction_0"]/div/div/div/div/div/div/div[1]/div/div[1]/a/text()')
        name_two = html.xpath('//*[@id="FILTERED_LIST"]/div/div/div/div/div[1]/div[2]/a/text()')
        # names = html.xpath('//*[@id="taplc_attraction_coverpage_attraction_0"]/div/div/div/div/div[1]/div/div[2]/a/@href')
        # names = ['https://www.tripadvisor.co.id' + item for item in names]

        # print(names)
        names = []
        names.extend(name_one)
        names.extend(name_two)
        print(len(names))
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_sights_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_sights_link_two.txt', 'r', encoding='utf-8')as f:
            for url in f:
                url = url.strip()
                url = url.replace('﻿', '')
                self.crawl(url)
                self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
