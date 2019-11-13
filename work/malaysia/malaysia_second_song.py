#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 15:45
# @Author  : yangmingming
# @Site    : 
# @File    : malaysia_second_song.py
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
        names = resp.html.xpath('//*[@id="mw-content-text"]/div/ol/li/a/text()')
        names = resp.html.xpath('//p/strong/text()')
        # print(resp.text)
        names = resp.html.xpath('//div[@style="text-align: justify;"]/text()')
        singer = []
        song = []

        for name in names[2:-1]:
            name = name.strip()
            if name and 'http' not in name:
                temp = name.split('-')
                singer.append(temp[0].strip())
                song.append(temp[-1].strip())
        self.save(singer, r"C:\Users\Administrator\Desktop\5.19 马来替换词网站\5.19 替换词网站\malaysia_second_txt\singer_name.txt")
        data = song
        return data

    def save(self, data: list, file=None):
        if data:
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
        url = 'https://ms.wikipedia.org/wiki/Senarai_lagu_rakyat_masyarakat_Melayu'
        url = 'http://www.gempak.com/artikel/2363/top-10-lagu-lagu-tempatan-menggunakan-nama-wanita'
        url = 'https://www.google.com/search?rlz=1C1NHXL_zh-CNCN747CN747&ei=Y4jfXPLbIMbosAevsqKYBQ&q=lagu+popular+malaysia+2019&oq=lagu+popular+malaysia+&gs_l=psy-ab.1.1.35i39j0i203l2j0i30l7.20127.20776..22221...0.0..0.222.848.2-4......0....1..gws-wiz.......0i5i30.4BDPv_N8h4Q'
        url = 'https://www.myinfotaip.com/2015/12/lagu-terbaru.html'
        path = r"C:\Users\Administrator\Desktop\5.19 马来替换词网站\5.19 替换词网站\malaysia_second_txt\song_name.txt"
        resp = self.crawl(url)
        data = self.parse(resp)
        self.save(data, file=path)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
