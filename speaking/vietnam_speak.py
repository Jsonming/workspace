#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:51
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_speak.py
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
        nodes = resp.html.xpath('//*[@id="tmTable"]/div/div[2]/span/span')
        for node in nodes:
            data.append(''.join(node.xpath(".//span/text()")))
        return data

    def save(self, data: list, file=None):
        if not file:
            file = r'C:\Users\Administrator\Desktop\name.txt'
        data = [item + '\n' for item in data]
        with open(file, 'a', encoding='utf-8')as f:
            f.write(''.join(data))

    def links(self) -> list:
        """
            Generate url
        :return: urls: list
        """
        with open('chinese_word.txt', 'r', encoding='utf8')as f:
            data = [item.strip() for item in f]
        return data[::-1]

    def run(self):
        links = self.links()
        for link in links:
            url = 'https://vi.glosbe.com/zh/vi/{}'.format(link)
            path = r"C:\Users\Administrator\Desktop\vietnam_speaking.txt"
            data = None
            try:
                resp = self.crawl(url)
                data = self.parse(resp)
            except:
                pass
            if data:
                self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
