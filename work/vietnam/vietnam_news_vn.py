#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 10:59
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_news_vn.py
# @Software: PyCharm

from requests_html import HTMLSession


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
        data = []
        names = resp.html.xpath('//*[@id="main_menu"]/a/@href')
        for name in names:
            class_name = name.split('/')
            if len(class_name) == 2:
                url = "https://vnexpress.net" + name
            elif len(class_name) == 4:
                url = name
            if url != "https://vnexpress.net/":
                data.append(url)
        return data

    def save(self, data: list, file=None):
        if not file:
            file = r'C:\Users\Administrator\Desktop\name.txt'
        with open(file, 'a', encoding='utf-8')as f:
            f.write('\n'.join(data))

    def links(self) -> list:
        """
            Generate url
        :return: urls: list
        """

    def run(self):
        # links = self.links()
        url = r'https://vnexpress.net'
        path = r""
        resp = self.crawl(url)
        data = self.parse(resp)
        self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
