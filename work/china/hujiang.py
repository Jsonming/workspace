#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 16:57
# @Author  : yangmingming
# @Site    : 
# @File    : hujiang.py
# @Software: PyCharm


import requests
import re
import pprint
import json
import time
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.content = None

    def crawl(self, off_number=None):
        url = "https://dict.hjenglish.com/jp/jc/{}".format(off_number)
        self.content = off_number
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'upgrade-insecure-requests': "1",
            'cookie': '_REF=; _REG=direct|; _SREF_20=; _SREG_20=direct|; HJ_UID=2b08b10f-dafb-bcba-e03a-bd8e643a7c76; Hm_lvt_d4f3d19993ee3fa579a64f42d860c2a7=1561962909; HJ_CSST_3=1; HJ_SID=10598d6a-c9bb-88b2-1cb8-51b1dcab461b; HJ_SSID_3=a73f1c91-2805-a100-1bda-57a34b9536c7; _SREF_3=; _SREG_3=direct|; HJ_CST=0; TRACKSITEMAP=3%2C20%2C'

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

        result = [self.content]
        html = etree.HTML(self.resp)
        pronounce_value = html.xpath('//span[@class="pronounce-value"]/text()')
        if pronounce_value:
            result.extend(pronounce_value)
        else:
            pronounces = html.xpath('//div[@class="pronounces"]/span[1]/text()')
            result.extend(pronounces)

        line = ','.join(result).replace(']', '').replace('[', '') + '\n'
        print(line)
        with open(r'C:\Users\Administrator\Desktop\Japanese_pronounce.txt', 'a', encoding='utf-8')as f:
            f.write(line)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        with open(r'C:\Users\Administrator\Desktop\校对.txt', 'r', encoding='utf8')as f:
            for word in f.readlines()[20000:]:
                time.sleep(2)
                content = word.strip()
                self.crawl(off_number=content)
                self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
