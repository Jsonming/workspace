#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 10:58
# @Author  : yangmingming
# @Site    : 
# @File    : korean_subtitle_zip.py
# @Software: PyCharm

import requests
from lxml.html import etree

headers = {
    "cookie": "__cfduid=dfa5a44a56e1f4818da6dc1c0442d32e61555031717; _"
              "ga=GA1.2.446599568.1555031722; trc_cookie_storage=taboola%2520global%253Auser-id%3Df47e0355-c5e3-4ac8-8d9c-69e65b8be1c0-tuct3a468dd; "
              "ShowSubtitleDetails=true; ShowSubtitlePreview=true; "
              "HearingImpaired=2; ForeignOnly=False; _gid=GA1.2.1534139390.1556500043; LanguageFilter=28; "
              "cookieconsent_dismissed=yes; cf_clearance=5c22147cf3e89737a1f9ac602ed6b8491cc6bc33-1556588618-31536000-150",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
with open('url.txt', 'r', encoding='utf8')as f:
    urls = f.readlines()

url_list = []
for index, url in enumerate(urls):
    url = url.strip()
    session = requests.session()
    resp = session.get(url=url, headers=headers)
    root = etree.HTML(resp.text)
    result = root.xpath('//div[@class="download"]/a/@href')
    result = ["https://subscene.com" + short_url for short_url in result]
    url_list.extend(result)

with open('download_url.txt', 'w', encoding='utf8')as f:
    f.writelines("\n".join(url_list))
