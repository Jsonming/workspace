#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 18:12
# @Author  : yangmingming
# @Site    : 
# @File    : korean_tv_two.py
# @Software: PyCharm


import requests
import json
import re
import execjs
from lxml import etree

pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://post.naver.com/async/my.nhn?memberNo=25909715&postListViewType=0&isExpertMy=true&fromNo={}&totalCount=140".format(
            off_number)
        # querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
        #                "offset": off_number}
        payload = ""

        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        print(url)
        response = requests.request("GET", url, data=payload, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        content = execjs.eval(self.resp)
        html = content.get('html')
        root = etree.HTML(html)
        tvs = root.xpath('//strong[@class="tit_feed ell"]//text()')
        for tv in tvs:
            name = pattern.sub("", tv)
            name = name.split('-')[-1]
            name = name.strip()
            macth = re.findall('[a-zA-Z0-9]+', name)
            if not macth:
                name = name.strip()
                names.append(name)
        print(names)
        self.save(names)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\tv_name_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        for i in range(1, 141):
            self.crawl(off_number=i)
            self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
