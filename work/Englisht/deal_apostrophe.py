#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 10:29
# @Author  : yangmingming
# @Site    : 
# @File    : deal_apostrophe.py
# @Software: PyCharm
from nltk.tokenize import word_tokenize


def select_aopstrophe():
    file_name = r"C:\Users\Administrator\Desktop\ebook_sentence_new.txt"
    with open(file_name, 'r', encoding='utf8')as f:
        for line in f:
            yield line


def apostrophe_index(string_list):
    """
    判断是否有单引号，如果有单引号，把单引号索引（不准确）放到列表里面。用于判断是否有单引号
    :param string_list: 字符串列表
    :return: 索引列表
    """
    apostrophe_index, string_length = [], 0
    for word in string_list:
        if word == "'":
            apostrophe_index.append(string_length)
        string_length += len(word)
    return apostrophe_index


def run():
    with open("ebook_sentence.txt", 'a', encoding='utf8')as f:
        for sentence in select_aopstrophe():
            words = word_tokenize(sentence)
            word_index = apostrophe_index(words)
            if not word_index:
                f.write(sentence)
                # print(sentence)


if __name__ == '__main__':
    run()
