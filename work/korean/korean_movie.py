#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 21:40
# @Author  : yangmingming
# @Site    : 
# @File    : korean_movie.py
# @Software: PyCharm

import requests
import json
import re
from lxml import etree
pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://book.naver.com/bookdb/book_detail.nhn?bid=7317415"
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
        root = etree.HTML(self.resp)
        content = root.xpath('//*[@id="tableOfContentsContent"]/p/text()')
        for name in content:
            name = pattern.sub('', name)
            macth = re.findall('[a-zA-Z0-9]+', name)
            if not macth:
                name = name.strip()
                self.result.append(name)

    def save(self):
        
        with open(r'C:\Users\Administrator\Desktop\movie_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
