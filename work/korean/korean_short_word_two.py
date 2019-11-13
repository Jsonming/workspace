#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 15:51
# @Author  : yangmingming
# @Site    : 
# @File    : korean_short_word_two.py
# @Software: PyCharm

import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, *args):
        url = "http://kr.qsbdc.com/krword2/wl.php?level={}&&tag=all&&page_id={}".format(*args)
        # url = "http://kr.qsbdc.com/krword2/wl.php?level=9&&tag=all&&page_id=39"
        # querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
        #                "offset": off_number}
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
        trs = root.xpath("//table//tr")
        for tr in trs:
            name = tr.xpath("./td[3]//text()")
            pronu = tr.xpath("./td[4]//text()")
            if name and name[0] != '韩语\n          ':
                short_word = name[0].strip()
                pronuncition = pronu[0].strip()
                self.result.append((short_word, pronuncition))

    def save(self):
        self.result = list(set(self.result))
        result = [item[0] for item in self.result]
        with open(r'C:\Users\Administrator\Desktop\korean_short_word_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))
        content = ["{}\t{}".format(item[0], item[1]) for item in self.result]
        with open(r'C:\Users\Administrator\Desktop\korean_short_word_proun.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(content))

    def run(self):
        # for t in range(1, 10):
        #     for p in range(1, 51):
        #         self.crawl(t, p)
        #         self.parser()
        # self.save()

        # for t in range(10, 11):
        #     for p in range(1, 30):
        #         self.crawl(t, p)
        #         self.parser()
        # self.save()

        # for t in range(11, 12):
        #     for p in range(1, 44):
        #         self.crawl(t, p)
        #         self.parser()
        # self.save()

        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
