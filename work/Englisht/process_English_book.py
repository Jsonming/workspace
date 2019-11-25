#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 18:22
# @Author  : yangmingming
# @Site    : 
# @File    : process_English.py
# @Software: PyCharm
import nltk
import json
from nltk.tokenize import sent_tokenize
from work.mylib.lib import delete_special_characters, contain_number, sentence_length, delete_extra_spaces
from work.mylib.lib import delete_url_link, delete_brackets_content, delete_brackets, replace_newline_characters
from work.mylib.mysql_my import MySql
from work.dingding.dingding_decorator import dingding_monitor
from work.Englisht.deal_apostrophe import apostrophe_index


class ProcessEnglish(object):
    def __init__(self):
        with open('CET4+6_edited.txt', 'r', encoding='utf8') as f:
            self.simple_word = set(f.read().split('\n'))

    def read_data(self):
        my = MySql()
        sql = """ select content from spiderframe.English_corpus_genlib limit 3;"""
        return my.get_many(sql)

    def contain_word(self, sentence):
        """
            判断单词包含
        :param sentence:
        :return:
        """
        special_char = ["?", ",", ".", "!", "'", "'m", "'d", "'re", "n't", "'s", "'ll", "'ve"]
        flag = [True if word.lower() in self.simple_word or word.lower() in special_char else False for word in
                sentence]
        return all(flag)

    @dingding_monitor
    def process_data(self):
        with open('ebook_sentence.txt', 'a', encoding='utf8') as s_f, open('ebook_num_sentence.txt', 'a',
                                                                           encoding='utf8') as n_f:
            for batch in self.read_data():
                for row in batch:
                    content = row[0]
                    content = delete_url_link(content)
                    content = delete_brackets_content(content)
                    content = delete_brackets(content)
                    content = replace_newline_characters(content)
                    content = delete_extra_spaces(content)
                    content = delete_special_characters(content)

                    sentences = sent_tokenize(content)
                    for sentence in sentences:
                        sentence_len = sentence_length(sentence)
                        if 5 <= sentence_len <= 15:
                            if not contain_number(sentence):
                                words = nltk.word_tokenize(sentence)
                                word_index = apostrophe_index(words)
                                if not word_index:
                                    s_f.write(sentence + "\n")
                            else:
                                n_f.write(sentence + "\n")

    @dingding_monitor
    def process_same_sentence(self):
        """
            处理句子，去除首尾引号
        :return:
        """
        finger_print = set()

        remove_before_file = 'ebook_num_sentence.txt'
        remove_after_file = "ebook_num_sentence_new.txt"
        with open(remove_before_file, 'r', encoding='utf8') as input_f, \
                open(remove_after_file, 'a', encoding='utf8') as output_f:
            for line in input_f:
                sentence = line
                new_sentence = sentence.capitalize()
                if new_sentence not in finger_print:
                    finger_print.add(new_sentence)
                    output_f.write(new_sentence + "\n")

    @dingding_monitor
    def process_diff(self):
        from work.mylib.lib import big_file_remove_same
        big_file_remove_same("contain_num.txt", "simple_sentence_num.txt")

    def output_mysql(self):
        with open(r'data.txt', 'a', encoding='utf8')as f:
            for batch in self.read_data():
                for row in batch:
                    content = {}
                    content["content"] = row[0]
                    data = json.dumps(content)
                    f.write(data + "\n")


if __name__ == '__main__':
    PE = ProcessEnglish()
    PE.output_mysql()
