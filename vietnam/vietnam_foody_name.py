#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 19:26
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_foody_name.py
# @Software: PyCharm
# !/usr/bin/env python
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
        url = "https://gappapi.deliverynow.vn/api/promotion/get_ids"
        payload = json.dumps({"promotion_status": 1, "sort_type": 0, "city_id": 217, "foody_service_id": 1})

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Referer": "https://www.foody.vn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Origin": "https://www.foody.vn",
            "X-Foody-Api-Version": "1",
            "X-Foody-App-Type": "1004",
            "X-Foody-Client-Type": "1",
            "X-Foody-Client-Version": "1",
            "X-Foody-Client-Language": "",
            "X-Foody-Client-Id": "",

        }
        # response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        print(self.resp)
        result = json.loads(self.resp).get("reply").get("promotion_ids")
        print(result)
        self.result = tuple(result)
        with open(r'C:\Users\Administrator\Desktop\food_id.txt', 'a', encoding='utf-8')as f:
            f.write(','.join([str(i) for i in result]))

    def save(self):
        result = list(set(self.result))
        with open(r'C:\Users\Administrator\Desktop\food_id.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join([str(i) for i in result]))

    def run(self):
        self.crawl()
        self.parser()
        # self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
