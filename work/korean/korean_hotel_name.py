#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 19:08
# @Author  : yangmingming
# @Site    : 
# @File    : korean_hotel_name.py
# @Software: PyCharm


import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.trivago.co.kr/?aDateRange%5Barr%5D=2019-05-25&aDateRange%5Bdep%5D=2019-05-27&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81322%2F200&iViewType=0&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=4&ra="
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'x-trv-cst:': "1443703219,1459869632,1472826866,25798,27291,32046,35446,37310,39578,39329,40428,42320,42304,43107,43759,42164,42280,42673,44629,44982,44964,43412,45265,45465,44432,45413,45433,39875,44394,45383,45749,45839,45038,46136,46138,46164,45295,46395,46378,46518,46568,46411,46480,46534,41697,46587,42107,46523",
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        print(self.resp)
        # response = json.loads(self.resp)
        # stores = response.get("accommodations")
        # for store in stores:
        #     store_name = store.get("name").get("value")
        #     names.append(store_name)
        self.result.extend(names)
        print(names)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
