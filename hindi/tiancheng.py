#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 14:45
# @Author  : yangmingming
# @Site    : 
# @File    : tiancheng.py
# @Software: PyCharm
from unicodedata import normalize


class HindiPro(object):
    def __init__(self):
        """
            印地语（天城文）音节处理
        """

    def read_content(self, file_path):
        with open(file_path, 'r', encoding='utf8') as f:
            for line in f:
                yield line.strip()

    def all_chars(self):
        file_path = r"C:\Users\Administrator\Desktop\印地语样例.txt"
        file_handle = self.read_content(file_path)

        chars = set()
        for line in file_handle:
            for char in line:
                chars.add(char)
        print(chars)

    def normal_test(self):
        file_path = r"C:\Users\Administrator\Desktop\词.txt"
        file_handle = self.read_content(file_path)
        for line in file_handle:
            print(line)
            print(len(line))
            print("*" * 100)
            result = normalize("NFKC", line)
            print(result)
            print(len(result))

    def word_gen(self, words):
        """
            字符串拼接
        :param chars:
        :return:
        """
        return '+'.join([''.join(word) for word in words]) + '\n'

    def run(self):
        file_path = r"C:\Users\Administrator\Desktop\印地语样例.txt"
        file_handle = self.read_content(file_path)

        vowel_mark = {'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'ऑ', 'औ', 'ऋ',
                      'ऍ'}

        consonant_mark = {'क', 'ख', 'ग', 'घ', 'ङ',
                          'च', 'छ', 'ज', 'झ', 'ञ',
                          'ट', 'ठ', 'ड', 'ढ', 'ण',
                          'त', 'थ', 'द', 'ध', 'न',
                          'प', 'फ', 'ब', 'भ', 'म',
                          'य', 'र', 'ल', 'व',
                          'श', 'ष', 'स', 'ह',

                          'ख़', 'क़', 'ग़', 'ज़', 'ड़', 'ढ़', 'फ़',
                          }
        consonant_singer_mark = {'ख़', 'क़', 'ज़', 'ड़', 'ढ़', 'फ़'}
        ignore_mark = {'ॐ'}
        vowel_correspon = {'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ', 'ृ': 'ऋ',
                           'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ'}

        number = {'१', '५', '९', '७', '६', '८', '३', '४', '२', '०'}
        s_char = {'्', 'ँ', 'ॆ', 'ः', 'ॅ', 'ं', 'ॉ'}
        r_char = {'़', }
        sum_char = set()
        for line in file_handle:
            line = normalize("NFC", line)
            words = []
            try:
                for char in line:
                    if char in vowel_mark or char in consonant_mark or char in ignore_mark:
                        words.append([char])
                    else:
                        words[-1].append(char)
            except Exception as e:
                pass

            new_words = []
            for i, word in enumerate(words):
                if len(word) > 1:
                    temp = []
                    for char in word:
                        if char in vowel_correspon:
                            word.remove(char)
                            temp.append([char])

                    if len(word) > 2:
                        for char in s_char:
                            if char in vowel_correspon:
                                word.remove(char)
                                temp.append([char])
                    new_words.append(word)
                    if temp:
                        new_words.extend(temp)
                else:
                    new_words.append(word)

            news_line = line + "=" + self.word_gen(new_words)
            with open(r'C:\Users\Administrator\Desktop\word_split.txt', 'a', encoding='utf8')as f:
                f.write(news_line)


if __name__ == '__main__':
    hp = HindiPro()
    hp.all_chars()
