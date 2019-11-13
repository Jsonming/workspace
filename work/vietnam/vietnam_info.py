#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 19:57
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_info.py
# @Software: PyCharm


import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):

        url = "https://gappapi.deliverynow.vn/api/promotion/get_infos"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}

        payload = json.dumps(
            {"promotion_ids": off_number, "sort_type": 2})

        headers = {
            "cache-control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
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
        # 将处理和去重的逻辑都放在这
        resp = json.loads(self.resp)
        infos = resp.get("reply", {}).get("promotion_infos")
        result = [restaurant.get("restaurant_info", {}).get("name") for restaurant in infos]
        print(result)
        self.result.extend(result)
        with open(r'C:\Users\Administrator\Desktop\food_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\food_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        with open(r'C:\Users\Administrator\Desktop\food_id.txt', 'r', encoding='utf-8')as f:
                data = f.read().split(',')
                for i in range(0, len(data), 10):
                    info_id = [int(in_id) for in_id in data[i:i+10]]
                    self.crawl(off_number=info_id)
                    self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
