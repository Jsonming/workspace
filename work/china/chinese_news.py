#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 17:45
# @Author  : yangmingming
# @Site    : 
# @File    : chinese_news.py
# @Software: PyCharm

from work.mylib.mysql_my import MySql
import re


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
        sql = "select content from spiderframe.china_news_people_content;"
        gen_data = self.read_data(sql)
        for batch in gen_data:
            for line in batch:
                content = line[0]

                sentences = chinese_sent(content)
                for sentence in sentences:
                    if 15 <= count_chinese_length(sentence) <= 20:
                        with open(r"C:\Users\Administrator\Desktop\china_news.txt", 'a', encoding='utf8')as f:
                            f.write(sentence.strip() + "\n")

    def deal_char(self, sentence):
        """
            删除掉含有不合法字符的句子
        :param sentence:
        :return:
        """
        leg_char = set(["。", "！", "？", "：", "，", "“", "”", "、"])
        if "_" in sentence:
            sentence = ""
        illeg_char = re.findall("\W", sentence)
        il_set = set(illeg_char)
        if il_set - leg_char:
            sentence = ""
        return sentence

    def deal_sentence(self):
        """
            处理中文句子
        :param sentence:
        :return:
        """
        sql = "select sentence from spiderframe.china_news_people_sentence;"
        data = self.read_data(sql)
        for s in data:
            for line in s:
                sentence = line[0].strip()
                sentence = self.deal_char(sentence)
                if sentence:
                    with open(r"C:\Users\Administrator\Desktop\china_news_sentence.txt", 'a', encoding='utf8') as f:
                        f.write(sentence + "\n")


if __name__ == '__main__':
    cn = ChineseNews()
    cn.deal_sentence()
