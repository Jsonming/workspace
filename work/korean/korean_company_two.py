#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 18:29
# @Author  : yangmingming
# @Site    : 
# @File    : korean_company_two.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree
pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "http://www.alba.co.kr"
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
        names = []
        html = etree.HTML(self.resp)
        companys_one = html.xpath('//*[@id="MainSuper"]/ul/li/a[1]/span[2]/text()')
        companys_two = html.xpath('//*[@id="MainSuperBrand"]/ul/li/a[1]/span[2]/text()')
        companys_three = html.xpath('//*[@id="MainGrand"]/ul/li/a/span[2]/text()')
        companys = []
        companys.extend(companys_one)
        companys.extend(companys_two)
        companys.extend(companys_three)
        for name in companys:
            name = pattern.sub('', name)
            macth = re.findall('[a-zA-Z0-9]+', name)
            if not macth:
                name = name.strip()
                print(name)
                self.result.append(name)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\korean_company_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()