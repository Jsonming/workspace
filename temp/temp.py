#!usrbinenv python
# -*- coding: utf-8 -*-
# @Time    : 2019623 15:45
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm


import requests
import re
import pprint
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "http://43.248.49.97/queryData/getQueryDataListByWhere?pageNum=1&pageSize=10&iEType=10&currencyType=rmb&year=2019&startMonth=5&endMonth=5&monthFlag=&codeTsFlag=true&codeLength=8&outerField1=CODE_TS&outerField2=ORIGIN_COUNTRY&outerField3=TRADE_MODE&outerField4=TRADE_CO_PORT&outerValue1=&outerValue2=&outerValue3=&outerValue4=&orderType=CODE+ASC"
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        html = etree.HTML(self.resp)
        field = html.xpath('//tr')
        for item in field:
            first_id = item.xpath('./div[1]/td[1]/div/text()')
            first_name = item.xpath('./div[1]/td[2]/div/text()')

            second_id = item.xpath('./div[2]/td[1]/div/text()')
            second_name = item.xpath('./div[2]/td[2]/div/text()')

            third_id = item.xpath('./div[3]/td[1]/div/text()')
            third_name = item.xpath('./div[3]/td[2]/div/text()')

            fourth_id = item.xpath('./div[4]/td[1]/div/text()')
            fourth_name = item.xpath('./div[4]/td[2]/div/text()')

            fifth_name = item.xpath('./td[1]/div/text()')
            sixth_name = item.xpath('./td[2]/div/text()')
            seven_id = item.xpath('./td[3]/div/text()')
            eigth_id = item.xpath('./td[4]/div/text()')
            ninth_name = item.xpath('./td[5]/div/text()')

            print(first_id, first_name)

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
