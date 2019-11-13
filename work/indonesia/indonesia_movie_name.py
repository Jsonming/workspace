#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 22:30
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_movie_name.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "https://www.filmdoo.com/element/feature_film/"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = {
            "explicit": 0,
            "page_name": "indonesian",
            "page": off_number,
            "offset": 32*(off_number-1),
            "attribute_id": 3742,
            "attributes_array": "",
            "attribute_logic": 0,
            "orderBy": "Latest_Date",
            "type": 0,
            "lazy_load": "true",
            "feature_film_id": ''
        }

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "referer": "https://www.filmdoo.com/indonesian/page/{}".format(off_number),
        }

        # response = requests.request("GET", url, data=payload, headers=headers)
        response = requests.request("POST", url, data=payload, headers=headers)
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
        html = etree.HTML(self.resp)
        names = html.xpath('//div[@class="move-film-title"]/text()')
        names = [item.strip() for item in names]
        print(names)
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_movie_one.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        for i in range(1, 18):
            self.crawl(i)
            self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
