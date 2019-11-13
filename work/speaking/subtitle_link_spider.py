#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:12
# @Author  : yangmingming
# @Site    : 
# @File    : subtitle_link_spider.py
# @Software: PyCharm
from requests_html import HTMLSession


class Spider(object):
    def __init__(self):
        pass

    def crawl(self, url):
        session = HTMLSession()
        headers = {
            'cache-control': "no-cache",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            'cookie': '__cfduid=d59a3342b6fc2bb43a85a227063f09b701560153431; _ga=GA1.2.747265340.1560153433; _gid=GA1.2.1127287720.1560153433; trc_cookie_storage=taboola%2520global%253Auser-id%3D0734ed6f-88a1-4e30-a44f-056afa930349-tuct3dad09b; LanguageFilter=45; HearingImpaired=2; ForeignOnly=False',
        }
        resp = session.get(url, headers=headers)
        return resp

    def parse(self, resp):
        """
            Parsing text content
        :param content: text content
        :return:
        """
        data = []
        links = resp.html.xpath('//*[@id="content"]/div[2]/div/table/tbody/tr/td[1]/a/@href')
        for link in links:
            url = "https://subscene.com" + link
            data.append(url)

        return data

    def save(self, data: list, file=None):
        if not file:
            file = r'C:\Users\Administrator\Desktop\name.txt'
        result = [item + '\n' for item in data]
        with open(file, 'a', encoding='utf-8')as f:
            f.write(''.join(result))

    def links(self) -> list:
        """
            Generate url
        :return: urls: list
        """

    def run(self):
        # links = self.links()
        for i in range(3, 101):
            url = 'https://subscene.com/browse/latest/all/{}'.format(i)
            path = r"vietnam_subtitle_link.txt"
            resp = self.crawl(url)
            data = self.parse(resp)
            self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
