#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 14:28
# @Author  : yangmingming
# @Site    : 
# @File    : subtitle_content_spider.py
# @Software: PyCharm
from requests_html import HTMLSession
import os


class Spider(object):
    def __init__(self):
        pass

    def crawl(self, url):
        session = HTMLSession()
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        resp = session.get(url, headers=headers)
        return resp

    def parse(self, resp) -> list:
        """
            Parsing text content
        :param content: text content
        :return:
        """
        download_url = None
        download_href = resp.html.xpath('//*[@id="downloadButton"]/@href')
        if download_href:
            download_url = "https://subscene.com" + download_href[0]
        return download_url

    def save(self, data: list, file=None):
        if not file:
            file = r'C:\Users\Administrator\Desktop\name.txt'
        with open(file, 'a', encoding='utf-8')as f:
            f.write('\n'.join(data))

    def download(self, url, name):
        session = HTMLSession()
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'cookie': '__cfduid=d59a3342b6fc2bb43a85a227063f09b701560153431; _ga=GA1.2.747265340.1560153433; _gid=GA1.2.1127287720.1560153433; trc_cookie_storage=taboola%2520global%253Auser-id%3D0734ed6f-88a1-4e30-a44f-056afa930349-tuct3dad09b; LanguageFilter=45; HearingImpaired=2; ForeignOnly=False',
        }
        resp = session.get(url, headers=headers)
        if not os.path.exists('./speak_file'):
            os.makedirs('./speak_file')
        with open('./speak_file/{}.zip'.format(name), 'wb') as f:
            f.write(resp.content)

    def links(self) -> list:
        """
            Generate url
        :return: urls: list
        """
        with open('vietnam_subtitle_link.txt', 'r', encoding='utf8')as f:
            data = f.readlines()

        return [item.strip() for item in data]

    def run(self):
        links = self.links()
        for url in links:
            print(url)
            resp = self.crawl(url)
            download_url = self.parse(resp)
            name = url.split('/')[-3]
            if download_url:
                self.download(download_url, name)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
