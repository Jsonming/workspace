#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 10:21
# @Author  : yangmingming
# @Site    :
# @File    : spider_pre_demo.py
# @Software: PyCharm

import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        #
        # https://www.doordash.com/food-delivery/bloomington-mn-restaurants/

        url = "https://vi.wikipedia.org/wiki/Th%C3%A0nh_ph%E1%BB%91_(Vi%E1%BB%87t_Nam)"

        # querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
        #                "offset": off_number}

        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # print(self.resp)
        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)
        # self.result.extend(names)

        response = etree.HTML(self.resp)
        city = response.xpath('//*[@id="mw-content-text"]/div/table/tbody//tr/td[2]/center/a/text()')
        city.extend(response.xpath('//*[@id="mw-content-text"]/div/table/tbody//tr/td[3]/center/a/text()'))
        city.extend(response.xpath('//*[@id="mw-content-text"]/div/table/tbody//tr/td[7]/center/a/text()'))
        city.extend(response.xpath('//*[@id="mw-content-text"]/div/table/tbody//tr/td[6]/center/a/text()'))

        self.result = list(set(city))

    def save(self):
        with open('name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
