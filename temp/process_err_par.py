#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 10:29
# @Author  : yangmingming
# @Site    : 
# @File    : process_err_par.py
# @Software: PyCharm


class Article:
    def __init__(self, name, occupied_area):
        # 定义属性
        self.name = name
        self.occupied_area = occupied_area
        print("有一个%s,占用面积是%.2f平方分米" % (self.name, self.occupied_area))


class Table:
    def __init__(self, name, desktop_area):
        # 定义属性
        self.name = name
        self.desktop_area = desktop_area
        self.usable_area = desktop_area
        self.desktop_article = []
        print("这是一张%s" % self.name)

    def add_article(self, article):
        if article.occupied_area > self.desktop_area:
            print("%s太大，无法放到%s上" % (article.name, self.name))
            return

        print("将%s放在%s上" % (article.name, self.name))
        self.desktop_article.append(article.name)
        self.usable_area -= article.occupied_area

    def __str__(self):
        return ("这个%s它的桌面面积是%.2f,\n现在可用面积是%.2f,\n桌面上放有%s。" % (
            self.name, self.desktop_area, self.usable_area, self.desktop_article[0]))


art1 = Article("小水杯", 5)
art2 = Article("手机", 4)
art3 = Article("电脑键盘", 12.5)
table1 = Table("电脑桌", 25)
table1.add_article(art1)
print(table1)
