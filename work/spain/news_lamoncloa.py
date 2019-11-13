#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 16:14
# @Author  : yangmingming
# @Site    : 
# @File    : news_lamoncloa.py
# @Software: PyCharm


import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        session = requests.session()

        url = "https://www.lamoncloa.gob.es/presidente/actividades/Paginas/index.aspx"
        query_string = {"mts": "201806"}
        payload = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            'MSOWebPartPage_PostbackSource': '',
            'MSOTlPn_SelectedWpId': '',
            'MSOTlPn_View': 0,
            'MSOTlPn_ShowSettings': 'False',
            'MSOGallery_SelectedLibrary': '',
            'MSOGallery_FilterString': '',
            'MSOTlPn_Button': 'none',
            '__REQUESTDIGEST': '0xB3A2BE5AD65D558389AE0DAA6B4AEF532CF87EFAC23622E74B26031D7062ED0A15B3B65E617D80A623C81A731EFD24D4DB98E8299C5A06937E76761E76C5818D,26 Jun 2019 10:18:15 -0000',
            'MSOSPWebPartManager_DisplayModeName': 'Browse',
            'MSOSPWebPartManager_ExitingDesignMode': 'false',
            'MSOWebPartPage_Shared': '',
            'MSOLayout_LayoutChanges': '',
            'MSOLayout_InDesignMode': '',
            'MSOSPWebPartManager_OldDisplayModeName': 'Browse',
            'MSOSPWebPartManager_StartWebPartEditingName': 'false',
            'MSOSPWebPartManager_EndWebPartEditing': 'false',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '/wEPDwUJMjM1MTk2OTQ1ZGSBXKbYgTNGdvaeSn9YdvTYHR3V/ep+Jc7XGG+sNY5yvA==',
            '__VIEWSTATEGENERATOR': '67358BEF',
            'ctl00$PlaceHolderHeader$ctl00$DisplayMode$Idioms$SelectIdiomas': 0,
            '_searchTextFromTop': "",

            'ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24SummarySearchByDate%24EditModePanel%24ddlMonth': 6,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24SummarySearchByDate%24EditModePanel%24ddlYear": 2018,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24hdnResultsCount": 40,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24hdnFilterDate": 201806,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24hdnFilterMinistry": -1,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnBackPage": '',
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnbtnPage1": 1,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnbtnPage2": 2,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnbtnPage3": 3,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnbtnPage4": 4,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnNextPage": 2,
            "ctl00%24PlaceHolderMain%24DisplayMode%24ctl00%24Summary%24EditModePanel%24ctl01%24hdnLastPage": 4,
            "__CALLBACKID": "ctl00$PlaceHolderMain$DisplayMode$ctl00$Summary",
            "__CALLBACKPARAM": 2,
            "__EVENTVALIDATION": "/wEdADaDajndvMpg1j9D+GtE+pvpicLH55vv6gBFB/M2W3Zyr87ZfHXjiXTgyZfmIrAtSn7laIC1jIz1yz7lz7iCUoRFzl1nqH1r4uDkhYRmQhw1dbkAjLBf+Foe9NYKgAAu3vrLqjvQS+LQKgc0q9Rnl/uD20nZWSC6zo759ahz4gCXNWrVkwKZ98KCqM6stRuZvrr67NsQq8b6upYGc3KFAMFWj+9D3F1K8p1mGe26A+nxb6qGOUNqFEiAA8t+LKqSrsM+Vv+LyW9KKQNi+8CkC+gmCav0xfd6qxa2MIWfeQctyDXcHUGb4hKl4lcDOyJ9Han+YIhx5iGYPeH3Gie+Kdo3FA7kum0vuFWQhTBdEu5lAHwdSnISso1a4sBcgWlaudh8XAr2S5ofEqfNHR7FPfOCcnHTWGmDngyiLK40j8aXTgN9bK8hSumcCzQghD3Rk3W7ncMLacqV5Ghlcvo7rUUsXisIKTOmN0RwsrUtlCEylIWQIKl4kMPG+97V52JiZbyO2AZR5bv2kwgWWPUUUcBrSP/TVlIVJTxAxACNTF0sUYSCa5YL5ms/4w23qKfLE2oEIgZpR0z479QDXi8i/qicoZJeWm5cMAzMSfKmRungmbCWM6hdaZSa2QbTafRtvLfl40rhV/IcFvSUBtM69WLWENCO2R76kupba6GrQXdHXYYdOFGhAYd/wLRamB047VDRpnXgUewzX5Xu1XXvNo+We06oUXnQcBt6D+Jca9eOWFLnM61J81/R340KNUDimT1mcKX8Q811yIOmgkUyR1hTTiNd+v4apk+rfJ16jlpkkM89MR+AcUHsf2GWx2Pq470yjZUeHGpc/LsbktDriDoPu1CdshZ4fWfbVb+AmNP9sd3htzPOXhHTnO+YqN8QU8abW7XdDUPd+w8OvENiIaPJ+o5gpGnJkkhz/2Uvg/eZcBUTVTX6/XadTiigtBmHwC0xsDZJYuWDNoyyDpyDGesyB1wP2IRfUq782W6uuaRCjw6jUh1holI/g8lNdnkmpNiQb9MfTMoymee+PDrGXRfXtKERuVvb5nZa4uWHVXZElohdGQWJUQ/UfBpmisqPrXrseNu5Tw1sjN2hySsIsp5KaOQoUMPTPkB0LeO36BAkdywsSKH7pyiqIAA5axgj7nKtCr9DT7EhKxV5jbh/8oPqvRl+QPiEe+WL5Cwvo4NO5g=="
        }

        headers = {
            "Accept": "*/*",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.lamoncloa.gob.es',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Referer': 'https://www.lamoncloa.gob.es/presidente/actividades/Paginas/index.aspx?mts=201806',
            'Origin': 'https://www.lamoncloa.gob.es',
            'Cookie': "_ga=GA1.3.1975160565.1561511172; _gid=GA1.3.232991838.1561511172; lang=es; _gali=ctl00_PlaceHolderMain_DisplayMode_ctl00_Summary_EditModePanel_ctl01_divPager",
            'Content-Length': "3465",
        }
        # response = session.get(url, headers=headers)
        response = requests.post(url, data=json.dumps(payload), headers=headers, params=query_string)
        self.resp = response.text

    def parser(self):
        html = etree.HTML(self.resp)
        link = html.xpath('//*[@id="columnContentContainer"]/ul/li[2]/div[2]/p[1]/a/@href')
        title = html.xpath('//*[@id="columnContentContainer"]/ul/li[2]/div[2]/p[1]/a/text()')
        # url = 'https://www.lamoncloa.gob.es' + link[0]
        # print(url)
        # print(title)
        print(self.resp)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
