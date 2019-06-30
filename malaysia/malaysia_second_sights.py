#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 15:24
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_second_sights.py
# @Software: PyCharm
from requests_html import HTMLSession


class Spider(object):
    def __init__(self):
        pass

    def crawl(self, url):
        session = HTMLSession()
        resp = session.get(url)
        return resp

    def parse(self, resp) -> list:
        """
            Parsing text content
        :param content: text content
        :return:
        """
        data = resp.html.xpath('//h3/span/text()')
        names = []
        for name in data:
            name = name[3:]
            print(name)
            names.append(name.strip())
        return names

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
        url = 'https://www.caridestinasi.com/tempat-menarik-penang/'
        url = 'https://www.caridestinasi.com/tempat-menarik-ipoh/'
        url = 'https://www.caridestinasi.com/tempat-menarik-perak/'
        path = r"C:\Users\Administrator\Desktop\5.19 马来替换词网站\5.19 替换词网站\malaysia_second_txt\singhts_name.txt"
        resp = self.crawl(url)
        data = self.parse(resp)
        self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()

