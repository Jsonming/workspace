#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 15:45
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm
# coding=utf-8
# import pymongo, time, requests, json, os
# import urllib.parse
import redis, pexpect
# def app_mongo():
#     mon = pymongo.MongoClient("mongodb://integrate:" + urllib.parse.quote_plus(
#         "integ_190228_snv738v8220aiVK9V820@_eate") + "@172.26.26.132:20388/integrate")
#     return mon
# mon_app = app_mongo()
# def mongodb():
#     mongo = pymongo.MongoClient(
#         "mongodb://xhql:" + urllib.parse.quote_plus(
#             "xhql_190228_snv738J72*fjVNv8220aiVK9V820@_") + "@172.26.26.132:20388/webpage")['webpage']
#     return mongo
# mongo = mongodb()
# def Baike():
#     webnum = mongo.baike_details.find({'state_qiu': 0}).count()
#     print(webnum)
#     filetime = time.strftime("%Y%m%d", time.localtime())
#     filename = 'inc_baike_{}.dat'.format(filetime)
#     filename = 'inc_baike_20190423.dat'
    # f = open(r'/mnt/data/liqiu/baike/{}'.format(filename), 'a', encoding='utf-8')
    # for i in range(0, webnum, 10000):
    #     print('*****************************************', i)
    #     filetime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    #     filename = 'full_{}.dat'.format(filetime)
    #     f = open(r'/mnt/data/liqiu/{}'.format(filename),'a',encoding='utf-8')
        # zds = mongo.baike_details.find({'state_qiu': 0}).limit(10000).skip(i)
        # for one in zds:
        #     try:
        #         liqiu_dict = {'id': str(one['id']), 'link': str(one['id']), 'title': str(one['title']),
        #                       'author': str(one['author']), 'content': str(one['content_np']),
        #                       'site_name': str(one['site_name']), 'article_url': str(one['article_url']),
        #                       'crawl_time': str(one['crawl_time']), 'source': str(one['source']), 'topic': '',
        #                       'flag': '0'}
        #         if one.get('type', []) and isinstance(one['type'], list):
        #             liqiu_dict['type'] = ' '.join(one['type'])
        #         elif one.get('type', '') and isinstance(one['type'], str):
        #             liqiu_dict['type'] = one['type']
        #         else:
        #             liqiu_dict['type'] = ''
        #             if one.get('label', []) and isinstance(one['label'], list):
        #                 liqiu_dict['label'] = ' '.join(one['label'])
        #             elif one.get('label', "") and isinstance(one['label'], str):
        #                 liqiu_dict['label'] = one['label']
        #             else:
        #                 liqiu_dict['label'] = ''
                    # if len(liqiu_dict)==0:
                    #     continue
                    # cons = liqiu_dict['content']
                    # url = 'http://172.26.26.135:8995/topic?content={}'.format(cons)
                    # ai = requests.get(url).text
                    # print(ai)
                    # if ai == 'AI':
                    #     ai = 'ai'
                    # else:
                    #     ai = ''
                    # liqiu_dict['topic'] = ai
                    #
                    # read_dat(liqiu_dict)
                    # f.write('{}\n'.format(json.dumps(liqiu_dict, ensure_ascii=False)))
                #
                # except KeyError as e:

                # print('异常')
                # print('---------------------------', e)