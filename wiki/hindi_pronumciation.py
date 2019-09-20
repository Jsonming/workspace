#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 17:38
# @Author  : yangmingming
# @Site    : 
# @File    : hindi_pronumciation.py
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
        url = "https://en.wiktionary.org/wiki/Appendix:Hindi_pronunciation"
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
        IPA_table_row = html.xpath('//table[@rules="all"]/tbody/tr')
        with open('hindi_pronumciation.txt', 'a', encoding='utf8') as f:
            # for row in IPA_table_row:
            #     th = row.xpath('./th//text()')
            #     td = row.xpath('./td')
            #     if td:
            #         td_one = ''.join(td[0].xpath('.//text()')).strip()
            #         td_two = ''.join(td[1].xpath('.//text()')).strip()
            #         td_three = ''.join(td[2].xpath('.//text()')).strip()
            #         td_four = ''.join(td[3].xpath('.//text()')).strip()
            #         f.write("    ".join((td_one, td_two, td_three, td_four, '\n')))
            #     else:
            #         f.write("    ".join(th))
            f.write(self.resp)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
