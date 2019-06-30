#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 17:15
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_short_word.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        # url = "https://salamadian.com/kosakata-bahasa-inggris/"
        url = "http://www.kamusmufradat.com/2017/10/kosakata-bahasa-arab.html"
        url = "https://www.caramudahbelajarbahasainggris.net/2013/04/ribuan-kosakata-bahasa-inggris-sehari-hari-dan-artinya.html"
        url = "http://cn.nemoapps.com/phrasebooks/indonesian"
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
        # names = html.xpath('//table/tbody/tr/td[3]//text()')

        # names = html.xpath('//*[@id="post-body-306764103926191667"]/div[10]/ol/li/span/text()')
        # name = html.xpath('//*[@id="post-body-306764103926191667"]/div[10]/div[2]/div/ol/span/li/text()')
        # new = []
        # new.extend(names)
        # new.extend(name)
        # new = [item.replace('(', '').replace(')', '').replace('.', '').strip() for item in new]
        # new = [item for item in new if item]

        # name_one = html.xpath('//*[@id="tablepress-80"]/tbody/tr/td[2]/text()')
        # name_two = html.xpath('//*[@id="tablepress-81"]/tbody/tr/td[2]/text()')
        # name = []
        # name.extend(name_one)
        # name.extend(name_two)

        name = html.xpath('//td[@class="scripts-column"]/div[1]/strong/text()')
        print(name)
        self.save(name)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_short_word_four.txt', 'w', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
