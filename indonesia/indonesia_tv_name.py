#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 20:24
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_tv_name.py
# @Software: PyCharm

import requests
import re
import json
from lxml import etree
import os


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        # url = "https://id.wikipedia.org/wiki/Kategori:Serial_televisi_Indonesia"
        # url = "https://m.iflix.com/browse/tv"
        # url ='https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/comedy","nextContent":"eyJvZmZzZXQiOjZ9"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url ='https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/comedy","nextContent":"eyJvZmZzZXQiOjE0fQ=="}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = "https://m.iflix.com/collections/genres/action"
        # url = "https://m.iflix.com/collections/genres/anime"
        # url = "https://m.iflix.com/collections/genres/comedy"
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/comedy","nextContent":"eyJvZmZzZXQiOjZ9"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/comedy","nextContent":"eyJvZmZzZXQiOjE0fQ=="}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = "https://m.iflix.com/collections/genres/crime"
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/crime","nextContent":"eyJvZmZzZXQiOjZ9"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/crime","nextContent":"eyJvZmZzZXQiOjE0fQ=="}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = "https://m.iflix.com/collections/genres/sports"
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/sports","nextContent":"eyJvZmZzZXQiOjZ9"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'
        # url = 'https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/sports","nextContent":"eyJvZmZzZXQiOjE0fQ=="}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}'

        url = off_number
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        # response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        print(self.resp)
        try:
            names = []
            response = json.loads(self.resp)
            stores = response.get("data").get("pageByUrl").get("content").get("items")
            for store in stores:
                store_name = store.get("assets")
                if store_name:
                    store_name = store_name.get("items")
                    for store in store_name:
                        name = store.get("title")
                        names.append(name)
        except:
            html = etree.HTML(self.resp)
            names = html.xpath('//div[@class="PosterLabelstyled__PosterLabel-sc-1ke1lrh-0 eNXuya"]/text()')
        print(names)
        print(len(names))
        self.save(names)

    def save(self, result):
        folder = r'C:\Users\Administrator\Desktop\indonesia_temp'
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\movie_name_two.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        class_type = ['action', 'chinese', 'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy', 'hindi',
                      'horror', 'indonesia', 'kids', 'korean', 'malay', 'music', 'romance', 'sci-fi', 'sports',
                      'thriller']
        urls = []
        for type_one in class_type:
            url = "https://m.iflix.com/collections/genres/{}".format(type_one)
            url_two = """https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/%s","nextContent":"eyJvZmZzZXQiOjZ9"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}""" % (type_one, )
            url_three = """https://m.iflix.com/api/gateway/graphql?operationName=PageByUrl&variables={"bgHeight":820,"bgLandscapeHeight":540,"bgLandscapeWidth":960,"bgWidth":545,"posterLandscapeHeight":540,"posterLandscapeWidth":960,"posterPortraitHeight":328,"posterPortraitWidth":218,"postersLimit":25,"totalContent":8,"url":"/genres/%s","nextContent":"eyJvZmZzZXQiOjE0fQ=="}&extensions={"persistedQuery":{"version":1,"sha256Hash":"060b4d0906f57de5e0159b0b8036c867f27bea0a97439453ceedeb17ed8b1663"}}""" % (type_one,)
            urls.append(url)
            urls.append(url_two)
            urls.append(url_three)

        for url in urls:

            self.crawl(url)
            self.parser()




if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
