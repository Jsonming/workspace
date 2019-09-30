#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 14:21
# @Author  : yangmingming
# @Site    : 
# @File    : hindi_tran.py
# @Software: PyCharm
from unicodedata import normalize


class HindiIPA(object):
    def __init__(self):
        self.vowel_chars = {'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'ऑ', 'औ', 'ऋ'}
        self.vowel_chars_double = {'अं', 'अः', 'अँ'}
        # 上面都是元音以及元音变音
        self.consonant_char = {'क', 'ख', 'ग', 'घ', 'ङ',
                               'च', 'छ', 'ज', 'झ', 'ञ',
                               'ट', 'ठ', 'ड', 'ढ', 'ण',
                               'त', 'थ', 'द', 'ध', 'न',
                               'प', 'फ', 'ब', 'भ', 'म',
                               'य', 'र', 'ल', 'व',
                               'श', 'ष', 'स', 'ह'}
        self.addition_consonants = {'ख़', 'क़', 'ग़', 'ज़', 'ड़', 'ढ़', 'फ़', "झ़"}
        self.ignore = {'ॐ', 'य़', '्'}
        self.simplify_vowel = {'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'े', 'ै', 'ॉ', 'ो', 'ौ',
                               'ँ', 'ं', 'ः', 'ॅ'}

    def read_content(self, file_path):
        with open(file_path, 'r', encoding='utf8') as f:
            for line in f:
                yield line.strip()

    def word_split(self, word):
        return [char for char in word]

    def process_word(self, word):
        """
            处理单词分隔
        :param word: 接收一个单词
        :return:
        """

    def run(self, file_path):
        content = self.read_content(file_path)
        for word in content:
            self.process_word(word)


if __name__ == '__main__':
    ha = HindiIPA()
    file_path = r"C:\Users\Administrator\Desktop\印地语样例.txt"
    ha.run(file_path)
