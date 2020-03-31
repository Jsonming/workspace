#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 9:58
# @Author  : yangmingming
# @Site    : 
# @File    : multi_language.py
# @Software: PyCharm
import json
import re
import os
from nltk import tokenize
# from hebrew_tokenizer import tokenize
from pythainlp.tokenize import sent_tokenize, word_tokenize

from work.mylib.lib import delete_special_characters, contain_number, delete_extra_spaces, chinese_sent
from work.mylib.lib import delete_url_link, delete_brackets_content, delete_brackets, replace_newline_characters
from work.mylib.mysql_my import MySql
from work.dingding.dingding_decorator import dingding_monitor


class MultiLanguage(object):
    """
    多国语言处理
    """

    def __init__(self):
        pass

    def output_data(self, table_name=None, file_name=None, test=None):
        """
        导出数据
        :param table_name:
        :param file_name:
        :return:
        """
        if not test:
            sql = """select * from spiderframe.{};""".format(table_name)
        else:
            sql = """select * from spiderframe.{} limit 3;""".format(table_name)

        my = MySql()
        with open(file_name, 'a', encoding='utf8')as f:
            for batch in my.get_many_json(sql):
                for item in batch:
                    content = {}
                    content_str = item.get("content")
                    if content_str:
                        content["content"] = content_str
                        data = json.dumps(content)
                        f.write(data + "\n")

    def delete_english(self, content):
        """
        删除文本中的英语
        :param content:
        :return:
        """
        return re.sub('[a-zA-Z]', '', content)

    def process_thai(self, content, sent_file):
        """
        处理泰语
        :param content:
        :return:
        """
        sentences = set()
        content = self.delete_english(content)  # 删除英语
        with open(sent_file, 'a', encoding='utf8') as s_f:
            sents = sent_tokenize(content)
            for sent in sents:
                if sent:
                    sentence_length = word_tokenize(sent)
                    if 7 <= len(sentence_length) <= 15:
                        if not contain_number(sent):
                            if sent not in sentences:
                                sentences.add(sent)
                                s_f.write(sent + "\n")

    def process_hebrew(self, content, sent_file):
        """
        处理希伯来语
        :param content:
        :param sent_file:
        :return:
        """
        sentences = set()
        content = self.delete_english(content)  # 删除英语
        with open(sent_file, 'a', encoding='utf8') as s_f:
            sents = tokenize(content)
            for sent in sents:
                # if sent:
                #     sentence_length = word_tokenize(sent)
                #     if 7 <= len(sentence_length) <= 15:
                #         if not contain_number(sent):
                #             if sent not in sentences:
                #                 sentences.add(sent)
                #                 s_f.write(sent + "\n")
                print(sent)

    def process_nltk(self, content, sent_file, language):
        """
        处理瑞典语用nltk
        :param content:
        :param sent_file:
        :return:
        """
        from nltk import tokenize
        sentences = set()
        with open(sent_file, 'a', encoding='utf8') as s_f:
            sents = tokenize.sent_tokenize(content, language=language)
            for sent in sents:
                if sent:
                    sentence_length = tokenize.word_tokenize(sent)
                    if 7 <= len(sentence_length) <= 15:
                        if not contain_number(sent):
                            if sent not in sentences:
                                sentences.add(sent)
                                s_f.write(sent + "\n")

    def process_chinese(self, content, sent_file, language):
        """
        处理中文
        :param content: 文本内容
        :param sent_file: 句子文件
        :param language: 语种
        :return:
        """
        sentences = set()
        with open(sent_file, 'a', encoding='utf8') as s_f:
            sents = chinese_sent(content)
            for sent in sents:
                if sent:
                    sentence_length = str(len(sent))
                    if sent not in sentences:
                        sentences.add(sent)
                        s_f.write(sentence_length + "\t" + sent + "\n")

    # @dingding_monitor
    def process_data(self, read_file, output_file):
        """
        处理数据
        : param
        read_file: 读取本地文件
        :param
        sent_file: 句子文件
        :param
        num_file: 包含数字的句子文件
        :
        return:
        """
        with open(read_file, 'r', encoding='utf8') as r_f:
            for line in r_f:
                data = json.loads(line.strip())
                content = data.get("content")
                content = delete_url_link(content)  # 去除文中url
                content = delete_brackets_content(content)  # 去除文件空格
                content = delete_brackets(content)
                content = replace_newline_characters(content)
                content = delete_extra_spaces(content)  # 处理后文件的空格
                content = delete_special_characters(content)  # 去除特殊字符

                # 以下是处理各个语言
                # self.process_thai(content, output_file)  # 处理泰语
                # self.process_hebrew(content, output_file)  # 处理希伯来语

                # self.process_nltk(content, output_file, language)
                self.process_chinese(content, output_file, language)

    def count_result(self, file):
        """
        统计结果数量
        :return:
        """
        num = 0
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                num += 1
        print(num)

    def thai_split(self, read_file, output_file):
        """
        泰语分词
        :param
        file:
        :return:
        """
        word_set = set()
        with open(read_file, 'r', encoding="utf8") as f, open(output_file, 'a', encoding="utf8")as w_f:
            for line in f:
                sentence = line.strip()
                words = word_tokenize(sentence)
                for word in words:
                    if word not in word_set:
                        w_f.write(word + "\n")
                        word_set.add(word)

    def split_word(self, file, output_file):
        """
        分词
        :param
        file:
        :return:
        """
        self.thai_split(file, output_file)
        self.count_result(output_file)

    def sort_sent(self, file):
        """
        排序文件
        :param file:
        :return:
        """

        with open(file, 'r', encoding='utf8') as f:
            content = [[int(line.split("\t")[0]), line] for line in f.readlines()]

        new_content = sorted(content, key=lambda x: x[0])
        with open("temp_" + file, 'a', encoding='utf8') as n_f:
            for item in new_content:
                n_f.write(item[1])


if __name__ == '__main__':
    ml = MultiLanguage()

    tables = [
        # "text_thai_dailynews_agriculture_content",
        # "text_thai_dailynews_article_content",
        # "text_thai_dailynews_economic_content",
        # "text_thai_dailynews_education_content",
        # "text_thai_dailynews_entertainment_content",
        # "text_thai_dailynews_it_content",
        # "text_thai_dailynews_sports_content",
        # "text_thai_dailynews_women_content",
        # "text_thailand_thairath_content",

        # "hebrew_walla_content",

        # "sweden_aftonbladet_content",
        # "sweden_sydsvenskan_content",

        # "Norway_aftenposten_content",
        # "Norway_dagbladet_content",
        # "Norway_dn_content"

        "text_china_ruiwen_content",
        "text_china_yifan_content",
        "text_chian_gushi365_content",

    ]

    # language = tables[0].split("_")[1]
    # temp_file = "{}_data.json".format(language)
    # sentence_file = '{}_sentence.txt'.format(language)
    # word_file = '{}_word.txt'.format(language)
    #
    # test_flag = False  # 测试 or 正式
    #
    # for table in tables:
    #     table_name = table.strip()
    #     ml.output_data(table_name=table_name, file_name=temp_file, test=test_flag)
    #
    # ml.process_data(temp_file, sentence_file)
    # ml.count_result(sentence_file)

    # ml.split_word(sentence_file, word_file)
    # os.remove(temp_file)

    ml.sort_sent("china_sentence.txt")
