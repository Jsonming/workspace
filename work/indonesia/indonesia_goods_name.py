#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 15:31
# @Author  : yangmingming
# @Site    : 
# @File    : indonesia_goods_name.py
# @Software: PyCharm


import requests
import re
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None

    def crawl(self, off_number=None):
        url = "https://gql.tokopedia.com/graphql"
        querystring = {"delivery_city_slug": "ramsey-ny-restaurants", "store_only": "true", "limit": "50",
                       "offset": off_number}
        payload = [{"operationName": "RecommendationQuery",
                    "query": "query RecommendationQuery($recomID: Int, $count: Int!, $page: Int!) {  get_home_recommendation {    recommendation_tabs {      id      name      image_url      __typename    }    recommendation_product(recomID: $recomID, count: $count, page: $page) {      product {        id        name        url        click_url        imageURL: image_url        wishlisted: is_wishlist        is_rating        is_shop        is_topads        discount_percentage        tracker_image_url        price        price_int        slashed_price        slashed_price_int        rating        countReview: count_review        recommendation_type        shop {          id          name          url          city          __typename        }        labels {          title          color          __typename        }        badges {          title          image_url          __typename        }        __typename      }      __typename    }    __typename  }}",
                    "variables": {"page": 5}
                    }]
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        # response = requests.request("GET", url, data=payload, headers=headers)
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        self.resp = response.text

    def parser(self):
        # 将处理和去重的逻辑都放在这
        # names = []
        # response = json.loads(self.resp)
        # stores = response.get("stores")
        # for store in stores:
        #     store_name = store.get("business").get("name")
        #     names.append(store_name)

        # print(self.resp)
        # html = etree.HTML(self.resp)
        # names = html.xpath()
        # self.save(names)
        pass

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
