#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 16:09
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_booking_hotel.py
# @Software: PyCharm

import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.booking.com/searchresults.vi.html"

        querystring = {"aid": "334565", "label": "baidu-brandzone_booking-brand-list1",
                       "sid": "1aeea660f564ce0224739b332e912b51", "tmpl": "searchresults", "ac_click_type": "b",
                       "ac_position": "0", "checkin_month": "4", "checkin_monthday": "26", "checkin_year": "2019",
                       "checkout_month": "5", "checkout_monthday": "16", "checkout_year": "2019", "class_interval": "1",
                       "dest_id": "230", "dest_type": "country", "dtdisc": "0", "from_sf": "1", "group_adults": "2",
                       "group_children": "0", "inac": "0", "index_postcard": "0", "label_click": "undef",
                       "no_rooms": "1", "postcard": "0", "raw_dest_type": "country", "room1": "A%2CA",
                       "sb_price_type": "total", "search_selected": "1", "shw_aparth": "1", "slp_r_match": "0",
                       "src": "index", "src_elem": "sb", "srpvid": "daeb385019570309", "ss": "Vietnam", "ss_all": "0",
                       "ss_raw": "vietnam", "ssb": "empty", "sshis": "0", "rows": "15", "offset": off_number}
        payload = ""
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        self.resp = response.text

    def parser(self):
        response = etree.HTML(self.resp)
        hotel_name = response.xpath('//span[@class="sr-hotel__name\n"]/text()')
        self.result.extend([name.strip() for name in hotel_name])
        print(self.result)

    def save(self):
        result = list(set(self.result))
        with open(r'C:\Users\Administrator\Desktop\hotel_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        for i in range(0, 15*67, 15):
            self.crawl(off_number=i)
            self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()