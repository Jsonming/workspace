#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 15:45
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm

# 临时文件，将整理入库
import pandas as pd
from mylib.lib import read_file, list_file
from mylib.mysql_my import MySql


class Temp(object):
    def __init__(self):
        pass

    def run(self):
        folder = r"C:\Users\Administrator\Desktop\work_temp\Viet-news"
        files = list_file(folder)
        my = MySql()

        for file in files:
            pf = pd.read_excel(file, header=None)
            data = pf[0]

            # data = read_file(file)
            for line in data:
                sql = "insert into vietnam_news_zero(sentence) value (%s)"
                my.cursor.execute(sql, (line))
            my.connect.commit()
        my.connect.close()
        #
        # file = r"C:\Users\Administrator\Desktop\work_temp\vietnam_news_sentence\vietnam_news_sentence.txt"
        # data = read_file(file)
        # my = MySql()
        # for line in data:
        #     sql = "insert into vietnam_news_three(sentence) value (%s)"
        #     my.cursor.execute(sql, (line))
        # my.connect.commit()
        # my.connect.close()



if __name__ == '__main__':
    t = Temp()
    t.run()
