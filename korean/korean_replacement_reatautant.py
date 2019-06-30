#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 15:50
# @Author  : yangmingming
# @Site    : 
# @File    : korean_replacement_reatautant.py
# @Software: PyCharm

import requests
import json
from lxml import etree
import re

pattern = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|▷|◇|-|…|○|#|◆|⚽|♬|\*|\//+|\/|[①②③④⑤⑥⑦⑧]+|×|&|nbsp;|™|@", re.S)
pattern_two = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|'|“|”|‘|’|,|;|；|:|'|∼|\.""")
pattern_three = re.compile("[a-zA-Z0-9]+", re.S)


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "http://m.menupan.com/search/rest_list_item.asp?"
        # querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
        #                "offset": off_number}
        payload = {
            "pt": "rt",
            "pg": off_number,
            "pz": 25,
            "tc": 11000,
            "r_pg": 0,
            "r_acode": '',
            "dev_opt": '',
            "ar": '',
            "lat": '',
            "lng": ''
        }
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "upgrade-insecure-requests": "1",
            # "Cookie": "ASPSESSIONIDQSTQRQBR=MFGMKOPCHKGOJOGIDHGANOOO; _ga=GA1.2.464534037.1557043228; _gid=GA1.2.960811273.1557043228; NoMemSessionID=190505%5F803915442%2E51; cls_cookie_location=onepage%3D%2Franking%2Franking_list.asp%3Fpt%3Drt%26r_pg%3D3%26r_acode%3DH302581",
            "Referer": "http://m.menupan.com/ranking/ranking_list.asp",
            "X-Requested-With": "XMLHttpRequest"

        }
        # response = requests.request("GET", url, data=payload, headers=headers)
        response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text
        # print(response.text)

    def parser(self):
        # 将处理和去重的逻辑都放在这
        root = etree.HTML(self.resp)
        names = root.xpath('//p[@class="iteminfoname"]/text()')
        for name in names:
            name = re.sub(pattern, '', name)
            name = name.strip()
            match = re.findall("[a-zA-Z0-9]+", name)
            if not match:
                self.result.append(name)

    def save(self):
        self.result = list(set(self.result))
        with open(r'C:\Users\Administrator\Desktop\korean\restaurant_name.txt', 'w', encoding='utf-8')as f:
            f.write('\n'.join(self.result))

    def run(self):
        for i in range(1, 41):
            self.crawl(off_number=i)
            self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
