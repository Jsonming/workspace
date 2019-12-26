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
from work.mylib.redis_my import SSDBCon
from multiprocessing import Pool
import threading
from threading import Thread

flag = []


def aaa(db_name, sentence):
    mr = SSDBCon()
    global flag
    flag.append(mr.exist_finger(db_name, sentence))


class ProcessEnglish(object):
    def __init__(self):
        with open('CET4+6_edited.txt', 'r', encoding='utf8') as f:
            self.simple_word = set(f.read().split('\n'))

    def read_data(self):
        my = MySql()
        sql = """ select content from spiderframe.text_english_chinadaily_travel_content;"""
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
    def process_data(self, read_file, sent_file, num_file):
        with open(sent_file, 'a', encoding='utf8') as s_f, \
                open(num_file, 'a', encoding='utf8') as n_f, \
                open(read_file, 'r', encoding='utf8') as r_f:

            for line in r_f:
                data = json.loads(line.strip())
                content = data.get("content")
                content = delete_url_link(content)
                content = delete_brackets_content(content)
                content = delete_brackets(content)
                content = replace_newline_characters(content)
                content = delete_extra_spaces(content)
                content = delete_special_characters(content)

                sentences = sent_tokenize(content)
                for sentence in sentences:
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
    def process_diff(self, input_file=None, output_file=None):
        from work.mylib.lib import big_file_remove_same
        big_file_remove_same(input_file, output_file)

    @dingding_monitor
    def output_mysql(self, data_file):
        with open(data_file, 'a', encoding='utf8')as f:
            for batch in self.read_data():
                for row in batch:
                    content = {}
                    content["content"] = row[0]
                    data = json.dumps(content)
                    f.write(data + "\n")

    def filter_length(self, input_file=None, output_file=None):
        """
        句长筛选函数
        :param intput_file:输入文件
        :param outputfile: 输出文件
        :return:
        """
        with open(output_file, 'a', encoding='utf8') as f:
            for line in open(input_file, 'r', encoding='utf8'):
                sentence = line.strip()
                sentence_len = sentence_length(sentence)
                if 4 <= sentence_len <= 18:
                    f.write(sentence + "\n")

    def multi_db_repeat_sentence(self, input_file=None, output_file=None, diff_db=None, insert_db=None):
        """
        多库对比去重
        :param input_file:输入文件
        :param output_file: 输出文件
        :param diff_db: diff 库 list
        :param insert_db: 指纹插入库
        :return:
        """
        mr = SSDBCon()

        with open(output_file, 'a', encoding='utf8') as new_f:
            for line in open(input_file, 'r', encoding='utf8'):
                sentence = line.strip()
                # flag = [mr.exist_finger(db_name, sentence) for db_name in diff_db]
                global flag
                tasks = [Thread(target=aaa, args=(db_name, sentence)) for db_name in diff_db]
                [task.start() for task in tasks]
                [task.join() for task in tasks]
                print(flag)
                if any(flag):
                    print(sentence)  # 句子重复不用处理，不要了
                else:
                    new_f.write(sentence + "\n")
                    mr.insert_finger(insert_db, sentence)
                flag = []


if __name__ == '__main__':
    PE = ProcessEnglish()

    # output_file = r'chinadaily_content_data.txt'
    # PE.output_mysql(output_file)

    # read_file = r"chinadaily_content_data.txt"
    # output_file = r"chinadaily_sentence.txt"
    # output_num_file = r"chinadaily_num_sentence.txt"
    # PE.process_data(read_file, output_file, output_num_file)

    # input_file = "ebook_num_sentence.txt"
    # output_file = "ebook_num_sentence_filter.txt"
    # PE.filter_length(input_file=input_file, output_file=output_file)

    # input_file = "chinadaily_sentence.txt"
    # output_file = "chinadaily_sentence_temp.txt"
    # PE.process_diff(input_file, output_file)
    #
    # input_file = "chinadaily_num_sentence.txt"
    # output_file = "chinadaily_num_sentence_temp.txt"
    # PE.process_diff(input_file, output_file)
    #
    input_file = r"chinadaily_sentence_temp.txt"
    output_file = "chinadaily_sentence_new.txt"
    diff_db = ["corpus_ebook_fingerprint", "corpus_news_fingerprint", "corpus_recording_fingerprint",
               "corpus_translation_fingerprint", "corpus_speech_fingerprint"]
    insert_db = "corpus_news_fingerprint"
    PE.multi_db_repeat_sentence(input_file, output_file, diff_db, insert_db)

    input_file = r"chinadaily_num_sentence_temp.txt"
    output_file = "chinadaily_num_sentence_new.txt"
    diff_db = ["corpus_ebook_fingerprint", "corpus_news_fingerprint", "corpus_recording_fingerprint",
               "corpus_translation_fingerprint", "corpus_speech_fingerprint"]
    insert_db = "corpus_news_fingerprint"
    PE.multi_db_repeat_sentence(input_file, output_file, diff_db, insert_db)

