#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 10:56
# @Author  : yangmingming
# @Site    : 
# @File    : English_speech.py
# @Software: PyCharm

from work.mylib.mysql_my import MySql
from work.mylib import delete_brackets_content, delete_brackets, replace_newline_characters, \
    delete_extra_spaces, split_content, delete_special_characters, contain_number, sentence_length


class EnglishSpeech(object):
    """
        ted 英语演讲稿，拆分
    """

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
        content = delete_brackets_content(content)
        content = delete_brackets(content)
        content = replace_newline_characters(content)
        content = content.replace("\t", '')
        content = delete_extra_spaces(content)
        return content

    def run(self):
        """ 程序主要逻辑控制"""
        sql = "select content from spiderframe.English_speaking_ted_content where id<10;"
        gen_data = self.read_data(sql)
        for batch in gen_data:
            for line in batch:
                content = line[0]
                if content:
                    text = self.process_content(content)
                    sentences = split_content(text)
                    for sentence in sentences:
                        sentence = delete_special_characters(sentence)
                        if contain_number(sentence):
                            sentence = ""
                        if 8 < sentence_length(sentence) < 18:
                            with open('English_ted_speech.txt', 'a', encoding="utf8") as f:
                                f.write(sentence + "\n")


if __name__ == '__main__':
    es = EnglishSpeech()
    es.run()
