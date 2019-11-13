#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 15:12
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_hotel_name.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "https://www.traveloka.com/hotel/indonesia?id=2760098057401446760&adloc=id-id&kw=2760098057401446760_hotel%20indonesia&gmt=e&gn=g&gd=c&gdm=&gcid=326489323410&gdp=&gdt=&gap=1t1&pc=1&cp=2760098057401446760_HLO100003-COM-D-s_2760098057401446760_100003-H&aid=65738320072&wid=aud-308616686859:kwd-186689356&fid=&gid=9056704&kid=_k_Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcB_k_&gclid=Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcB"
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
        names = html.xpath('//*[@id="popularHotelList"]/div/div[2]/div/div[1]/h3/a/text()')
        # self.save(names)
        print(names)

        links = html.xpath('//*[@id="container"]/div[3]/div[4]/div[1]/div[3]/p/a/@href')
        print(links)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
