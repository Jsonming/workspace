#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 18:22
# @Author  : yangmingming
# @Site    : 
# @File    : process_English.py
# @Software: PyCharm

from mylib.lib import delete_url_link, delete_brackets_content, delete_brackets, replace_newline_characters
from mylib.lib import split_content
from mylib.mysql_my import MySql


class ProcessEnglish(object):
    def __init__(self):
        pass

    def read_data(self):
        my = MySql()
        sql = """ select content from spiderframe.English_corpus_gutenberg where id < 4;"""
        return my.get_many(sql)

    def process_data(self):
        for batch in self.read_data():
            for row in batch:
                content = row[0]
                content = delete_url_link(content)
                content = delete_brackets_content(content)
                content = delete_brackets(content)
                content = replace_newline_characters(content)
                content = replace_newline_characters(content)
                sentences = split_content(content)
                for sentence in sentences:
                    print(sentence)


if __name__ == '__main__':
    PE = ProcessEnglish()
    PE.process_data()
