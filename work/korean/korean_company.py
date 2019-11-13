#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 17:37
# @Author  : yangmingming
# @Site    : 
# @File    : korean_sights_two.py
# @Software: PyCharm


import requests
import re
import json
import time
from lxml import etree
pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=1&LinkNo=0&schType=0&schGid=0&Page={}".format(off_number)
        # url = "http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page={}".format(off_number)
        # url = "http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=3&LinkNo=0&schType=0&schGid=0&Page={}".format(off_number)

        print(url)
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
        companys = html.xpath('//*[@id="devStarterForm"]/div[2]/ul/li/div[1]/div[1]/a/text()')
        # companys = html.xpath('//*[@id="devStarterForm"]/div[2]/ul[2]/li/div/div/span/a/text()')
        print(len(companys))
        for name in companys:
            name = pattern.sub('', name)
            macth = re.findall('[a-zA-Z0-9]+', name)
            if not macth:
                name = name.strip()
                print(name)
                self.result.append(name)

    def save(self):
        with open(r'C:\Users\Administrator\Desktop\company_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        for i in range(10, 511):
            time.sleep(3)
            self.crawl(i)
            self.parser()
        # self.crawl()
        # self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
