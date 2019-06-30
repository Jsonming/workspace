#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 17:20
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_app.py
# @Software: PyCharm

import requests
import re
import json
import pprint
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        # url = "https://play.google.com/store/apps?hl=in"
        url = off_number

        response = requests.request("GET", url, headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)
        # self.result.extend(names)
        # print(self.resp)

        # 第一个网
        html = etree.HTML(self.resp)
        # names = html.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz[11]/c-wiz/div/div[1]/div[2]/a/@href')

        names = html.xpath('//div[@class="WsMG1c nnK0zc"]/text()')
        print(names)
        self.save(names)

        # 第二个网站
        # html = etree.HTML(self.resp)
        # content = html.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div/text()')
        # print(content)

        # 第三个网站
        # html = etree.HTML(self.resp)
        # name = html.xpath('//*[@id="main"]/section/div/ul/li/h3/a/text()')
        # self.save(name)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_app_one.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        # self.crawl()
        # self.parser()

        # with open(r'C:\Users\Administrator\Desktop\indonesia_app_link.txt', 'r', encoding='utf-8')as f:
        #     links = f.readlines()
        links = [
            # "https://play.google.com/store/apps/collection/cluster?clp=ogoKCAEqAggBUgIIAQ%3D%3D:S:ANO1ljJG6Aw&gsr=Cg2iCgoIASoCCAFSAggB:S:ANO1ljLKNqE&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogoKCAQqAggBUgIIAQ%3D%3D:S:ANO1ljLEbPM&gsr=Cg2iCgoIBCoCCAFSAggB:S:ANO1ljIL2pc&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY19GOTEyNk1hUnpLVRA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljKl4-Y&gsr=CiuiCigIARocChZyZWNzX3RvcGljX0Y5MTI2TWFSektVEDsYAyoCCAFSAggC:S:ANO1ljI9FJE&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY18yeHFtSWFsRGswRRA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljJbU0o&gsr=CiuiCigIARocChZyZWNzX3RvcGljXzJ4cW1JYWxEazBFEDsYAyoCCAFSAggC:S:ANO1ljJ1lOk&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY191Y0lGYUVUUmVTMBA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljKEE0E&gsr=CiuiCigIARocChZyZWNzX3RvcGljX3VjSUZhRVRSZVMwEDsYAyoCCAFSAggC:S:ANO1ljJcKlg&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogoKCAkqAggBUgIIAQ%3D%3D:S:ANO1ljKvIJM&gsr=Cg2iCgoICSoCCAFSAggB:S:ANO1ljKM8Jw&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY19vbDFxdl9tODloVRA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljLnmTE&gsr=CiuiCigIARocChZyZWNzX3RvcGljX29sMXF2X204OWhVEDsYAyoCCAFSAggC:S:ANO1ljJBunU&hl=in"
            # "https://play.google.com/store/apps/collection/cluster?clp=SisKKQojcHJvbW90aW9uXzMwMDE4MjNfc3Vic2NyaXB0aW9uX2FwcHMQBxgD:S:ANO1ljInn-o&gsr=Ci1KKwopCiNwcm9tb3Rpb25fMzAwMTgyM19zdWJzY3JpcHRpb25fYXBwcxAHGAM%3D:S:ANO1ljLeenA&hl=in"
        ]

        for link in links:
            link = link.strip()
            self.crawl(link)
            self.parser()

        # link = "https://play.google.com/store/apps/collection/cluster?clp=ChgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljKVCGg&gsr=ChoKGAoWChB0b3Bncm9zc2luZ19HQU1FEAcYAw%3D%3D:S:ANO1ljI_yc8"
        # self.crawl(link)
        # self.parser()

        # app第二个网站
        # url = "https://chrome.google.com/webstore/category/extensions?hl=id&_feature=android"
        # self.crawl(url)
        # self.parser()
        # 第二个网站没找到数据

        # 第三个网站
        # links = [
        #     "https://www.apple.com/id/itunes/charts/free-apps/",
            # "https://www.apple.com/id/itunes/charts/paid-apps/"
        # ]
        # for url in links:
        #     self.crawl(url)
        #     self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
