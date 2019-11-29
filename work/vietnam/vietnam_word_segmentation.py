#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 15:00
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_word_segmentation.py
# @Software: PyCharm
import string


class VietnamWordSegmentation(object):
    def __init__(self):
        pass

    def analysis_result(self, result_file=None):
        """
        将结果的多音节单词和单音节单词做区分
        :param result_file: 结果文件
        :return:
        """
        word_list_temp = set()
        with open(result_file, 'r', encoding='utf8')as f:
            for line in f:
                sentence = line.strip()
                if sentence:
                    words = sentence.split()
                    for word in words:
                        if word not in string.punctuation and "._." not in word:
                            word_list_temp.add(word)

        with open('single_word.txt', 'a', encoding='utf8')as s_f, \
                open("multi_word.txt", 'a', encoding='utf8')as m_f:
            for w in word_list_temp:
                if "_" in w:
                    w = w.replace("_", ' ')
                    m_f.write(w + "\n")
                else:
                    s_f.write(w + "\n")

    def diff_word(self, base_file=None, diff_file=None):
        """
        将分出来的词跟wordlist 做diff
        :diff_file 要跟wordlist对比的词文件
        :return:
        """
        word_list = set()
        word_file = base_file

        with open(word_file, 'r', encoding='utf8')as w_f:
            for line in w_f:
                word_list.add(line.strip().lower())

        word_list_temp = set()
        with open(diff_file, 'r', encoding='utf8')as d_f:
            for line in d_f:
                word = line.strip().lower()
                if word not in word_list:
                    word_list_temp.add(word)

        new_file = diff_file.split('.')[0] + "_new.txt"
        with open(new_file, 'a', encoding='utf8')as n_f:
            for w in word_list_temp:
                n_f.write(w + "\n")


if __name__ == '__main__':
    vws = VietnamWordSegmentation()
    # result_file = "result.txt"
    # vws.analysis_result(result_file=result_file)
    # vws.diff_word("multi_word.txt")
    # vws.diff_word("single_word.txt")
    vws.diff_word(diff_file=r"C:\Users\Administrator\Desktop\分词工具.txt")
