#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 14:44
# @Author  : yangmingming
# @Site    : 
# @File    : korean_replacement_app.py
# @Software: PyCharm


import requests
import json
import pprint
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        # url = "https://itunes.apple.com/kr/genre/ios/id36"
        url = off_number
        # querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
        #                "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'cookie': "geo=CN; ccl=z4l8bj6LMTWTSx83c6mgyA==; xp_ci=3zwxdEIzE2hz4bNzAkyznbDTDcB8",
            "upgrade-insecure-requests": "1",

        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text
        print(url)

    def parser(self):
        # 将处理和去重的逻辑都放在这
        root = etree.HTML(self.resp)
        # names = root.xpath('//div[@class="grid3-column"]//a/@href')
        names = root.xpath('//*[@id="selectedcontent"]/div/ul/li/a/text()')
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\korean_team\app_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        with open(r'C:\Users\Administrator\Desktop\korean_team\app_class_links.txt', 'r', encoding='utf-8')as f:
            links = f.readlines()
        for link in links:
            link = link.strip()
            self.crawl(link)
            self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
