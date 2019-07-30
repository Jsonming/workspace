#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 11:32
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_pron_dict.py
# @Software: PyCharm

import requests
import re
import pprint
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.url = None
        self.word = None

    def crawl(self, off_number=None):
        url = "https://vi.wiktionary.org/wiki/{}#Tiếng_Việt".format(off_number)
        self.url = url
        self.word = off_number
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

        pron_name = []
        html = etree.HTML(self.resp)
        first_line_add = html.xpath('//table[@class="wiktvi-vie-pron wikitable"]/tbody/tr[1]//a/text()')
        if first_line_add:
            first_line = html.xpath('//table[@class="wiktvi-vie-pron wikitable"]/tbody/tr[2]/td')
            if len(first_line) == 3:
                for pron in first_line:
                    first_line_name = ''.join(pron.xpath('./span[@class="IPA"]//text()'))
                    pron_name.append(first_line_name)
            else:
                tag = int(first_line[0].xpath('./@colspan')[0])
                if tag == 3:
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[1].xpath('./span[@class="IPA"]//text()')))
                elif tag == 1:
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[1].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[1].xpath('./span[@class="IPA"]//text()')))
                elif tag == 4:
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(first_line[0].xpath('./span[@class="IPA"]//text()')))

            second_line = html.xpath('//table[@class="wiktvi-vie-pron wikitable"]/tbody/tr[5]/td')
            if len(second_line) == 3:
                for pron in second_line:
                    second_line_name = ''.join(pron.xpath('./span//text()'))
                    pron_name.append(second_line_name)
            else:
                tag = int(second_line[0].xpath('./@colspan')[0])
                if tag == 3:
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[1].xpath('./span[@class="IPA"]//text()')))
                elif tag == 1:
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[1].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[1].xpath('./span[@class="IPA"]//text()')))
                elif tag == 4:
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))
                    pron_name.append(''.join(second_line[0].xpath('./span[@class="IPA"]//text()')))

            if len(pron_name) == 6:
                pron_name.insert(0, self.word)
                with open(r'correct_words.txt', 'a', encoding='utf8') as f:
                    f.write(','.join(pron_name) + "\n")
            else:
                print("*" * 180)
                print(pron_name)
                print(self.word)

        else:
            with open(r'empty_words.txt', 'a', encoding='utf8') as f:
                f.write(self.word + "\n")

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        words = []
        with open(r'900总_word.txt', 'r', encoding='utf8') as f:
            for line in f:
                words.append(line.split()[0])
        for word in words[171:]:
            self.crawl(off_number=word)
            self.parser()

        # self.crawl()
        # self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
