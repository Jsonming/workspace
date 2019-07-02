#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 17:45
# @Author  : yangmingming
# @Site    : 
# @File    : chinese_news.py
# @Software: PyCharm

from mylib.lib import *
from workspace.mylib.mysql_my import MySql


class ChineseNews(object):
    def __init__(self):
        pass

    def read_data(self, sql):
        """
            读取数据
        :return: 返回一个生成器对象
        """
        ms = MySql()
        return ms.get_many(sql)

    def process_content(self, content):
        """
            处理文章数据
        """
        # content = delete_brackets_content(content)
        # content = delete_brackets(content)
        content = replace_newline_characters(content, sep='')
        content = content.replace("\t", '')
        content = delete_extra_spaces(content)
        return content



    def run(self):
        """ 程序主要逻辑控制"""
        sql = "select content from spiderframe.china_news_people_content where id < 20;"
        gen_data = self.read_data(sql)
        for batch in gen_data:
            for line in batch:
                content = line[0]

                sentences = chinese_sent(content)
                for sentence in sentences:
                    print(repr(sentence))
                # text = self.process_content(content)
                # if text:
                #     try:
                #         sentences = split_content(text)
                #     except:
                #         print(text)
                #     else:
                #         for sentence in sentences:
                #             sentence = delete_special_characters(sentence)
                #             print(sentence)
                # print(repr(text))


if __name__ == '__main__':
    cn = ChineseNews()
    cn.run()
