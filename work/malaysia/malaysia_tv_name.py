#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 11:36
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_tv_name.py
# @Software: PyCharm.

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "https://www.google.com/search?rlz=1C1NHXL_zh-CNCN747CN747&ei=0zC3XM__H9XRxgOwyIqQCw&q=tv+malaysia&oq=&gs_l=psy-ab.1.5.35i39l6.77657.77657..80128...1.0..0.0.0.......0....1..gws-wiz.....6.dUc1mHOkw9I"
        # url = "https://www.google.com/search?q=filem+melayu&rlz=1C1NHXL_zh-CNCN747CN747&oq=filem+melayu&aqs=chrome..69i57.3566j0j7&sourceid=chrome&ie=UTF-8"
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
        print(self.resp)
        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)

        with open('b.html', 'w', encoding='utf-8')as f:
            f.write(self.resp)

        html = etree.HTML(self.resp)
        # names = html.xpath('//div[@class="mB12kf JRhSae ZyAH8d nDgy9d"]/text()')
        # names = re.findall(r'5\x22\x3e(.*?)\x3c/div\x3e\x3c/', self.resp)
        # print(names)
        # self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
