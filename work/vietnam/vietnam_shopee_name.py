#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 16:36
# @Author  : yangmingming
# @Site    : 
# @File    : shopee_name.py
# @Software: PyCharm
import requests
import json
import re
from lxml import etree
from urllib.parse import unquote


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://shopee.vn/api/v2/search_items"
        # url = "https://shopee.vn/api/v2/recommendation/hot_search_words?limit=28&offset=0"

        querystring = json.dumps({"by": "relevancy", "keyword": "sách",
                                  "limit": 50, "newest": 50, "ord": "desc", "page_type": "search"})

        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "referer": "https://shopee.vn/search?keyword=s%C3%A1ch&page=1&sortBy=relevancy",

            "if-none-match": "55b03-922335a53c4c1fb781cb18392bd75e5c",
            "pragma": "no-cache",
            "sec-fetch-mode": "cors",
            'x-api-source': "pc",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "cookie": '_gcl_au=1.1.108376856.1566871855; _med=cpc; csrftoken=7nJpUMsPVEM8VJUUT6Z3jbkFiztUDu9o; SPC_IA=-1; SPC_EC=-; SPC_U=-; REC_T_ID=e82427da-c86f-11e9-a048-52540005f038; SPC_F=PHhC2C8ZIPVFpgnsQHoLI3ukAS6wLVPD; welcomePkgShown=true; _hjid=7e857252-d7e0-4919-8ffa-357715191a74; _ga=GA1.2.1509814519.1566871869; _fbp=fb.1.1566872015210.90901393; _gcl_aw=GCL.1567146233.Cj0KCQjw7YblBRDFARIsAKkK-dJvrJvyUXGieAsT9k8FafREaKZeKP_zVr0P664Du1LseZi9O7QEFWMaAlqnEALw_wcB; SPC_SI=3vrdql371umgbzqwbnx3vexpcbjg0shs; _gid=GA1.2.1888109569.1567146249; _gac_UA-61914164-6=1.1567146249.Cj0KCQjw7YblBRDFARIsAKkK-dJvrJvyUXGieAsT9k8FafREaKZeKP_zVr0P664Du1LseZi9O7QEFWMaAlqnEALw_wcB; REC_MD_20=1567161001; REC_MD_14=1567161033; REC_MD_30_2000039439=1567161162; _dc_gtm_UA-61914164-6=1; SPC_T_IV="6JyEr0qHR5cvXGO/BZHNdw=="; SPC_T_ID="K8lK0XR0I3JWdr/I7myKSzJ4bH1iXyb55qEaaamaVAD5uKNmXqxz8hHy2WNcAF55xb3V6+oyXwgE7IblYPqPHzzST0iq2+p2Zl/ynv7jmJQ="',
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",


        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        self.resp = response.text

    def parser(self):
        # req_url = unquote(self.resp)
        # category = re.findall(r'keyword=(.*?)&', req_url)[0]
        print(self.resp)
        data = json.loads(self.resp)
        items = data.get("items")
        for item in items:
            image = item.get("image")
            url = "https://cf.shopee.vn/file/" + image
            print(url)

            # images = item.get("images")
            # for img in images:
            #     print(len(img))
            #     url = "https://cf.shopee.vn/file/" + img
            #     print(url)

    def save(self):
        stores_name = self.result
        with open('name.txt', 'a', encoding='utf-8')as f:
            for store_name in stores_name:
                f.write(store_name.strip())
                f.write(',')

    def run(self):
        self.crawl()
        self.parser()
        # self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
