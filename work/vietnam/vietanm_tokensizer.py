#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 16:41
# @Author  : yangmingming
# @Site    : 
# @File    : vietanm_tokensizer.py
# @Software: PyCharm

from pyvi import ViTokenizer, ViPosTagger


class VietanmToken(object):
    def __init__(self):
        pass

    def run(self, file):
        single_word, multi_word = set(), set()
        with open(file, 'r', encoding='utf8')as f:
            for line in f:
                sentence = line.strip()
                words = ViPosTagger.postagging(ViTokenizer.tokenize(sentence))[0]  # 获取分词结果
                for word in words:
                    if "_" in word:
                        multi_word.add(word)
                    else:
                        single_word.add(word)
        single_word_file = file.replace(".txt", "_single_word.txt")
        multi_word_file = file.replace(".txt", "_multi_word.txt")

        with open(single_word_file, 'a', encoding="utf8")as single_f:
            for single in single_word:
                single_f.write(single + "\n")

        with open(multi_word_file, 'a', encoding="utf8")as multi_f:
            for multi in multi_word:
                multi_f.write(multi.replace("_", " ") + "\n")


if __name__ == '__main__':
    file = r"C:\Users\Administrator\Desktop\talk.txt"

    VT = VietanmToken()
    VT.run(file)
