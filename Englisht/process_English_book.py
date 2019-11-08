#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 18:22
# @Author  : yangmingming
# @Site    : 
# @File    : process_English.py
# @Software: PyCharm

import nltk
from nltk.tokenize import sent_tokenize

from mylib.lib import delete_special_characters, contain_number, sentence_length, delete_extra_spaces
from mylib.lib import delete_url_link, delete_brackets_content, delete_brackets, replace_newline_characters
from mylib.mysql_my import MySql


class ProcessEnglish(object):
    def __init__(self):
        with open('CET4+6_edited.txt', 'r', encoding='utf8') as f:
            self.simple_word = set(f.read().split('\n'))

    def read_data(self):
        my = MySql()
        sql = """ select content from spiderframe.English_corpus_gutenberg;"""
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

    def process_data(self):
        with open('news_sentence.txt', 'a', encoding='utf8') as s_f, open('news_num_sentence.txt', 'a',
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
                                if self.contain_word(words):
                                    s_f.write(sentence + "\n")
                            else:
                                n_f.write(sentence + "\n")


if __name__ == '__main__':
    PE = ProcessEnglish()
    PE.process_data()
