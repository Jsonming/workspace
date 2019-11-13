#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 10:17
# @Author  : yangmingming
# @Site    : 
# @File    : korean_city.py
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
        for i in range(10,11):
            names = resp.html.xpath('//*[@id="mw-content-text"]/div/table[{}]/tbody/tr/td[2]/span/text()'.format(i))
            # names = resp.html.xpath('//*[@id="mw-content-text"]/div/ul[16]/li/span[2]/text()')
            # names = resp.html.xpath('//*[@id="mw-content-text"]/div/ul[17]/li/text()')
            # names = resp.html.xpath('//*[@id="mw-content-text"]/div/ul[17]/li/text()')
            for name in names:
                name = name.replace('（', '').replace('）', '').strip()
                print(name)

                data.append(name)
            print('*'*100)
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
        path = r'C:\Users\Administrator\Desktop\korean_school_name.txt'
        url = r"https://zh.wikipedia.org/wiki/韩国城市列表"
        # url = r"https://zh.wikipedia.org/wiki/韓國大學列表"
        resp = self.crawl(url)
        data = self.parse(resp)
        self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()