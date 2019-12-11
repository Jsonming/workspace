#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 17:03
# @Author  : yangmingming
# @Site    : 
# @File    : process_news.py
# @Software: PyCharm
import json
import nltk
from nltk.tokenize import sent_tokenize
from threadpool import ThreadPool, makeRequests
from work.mylib.mysql_my import MySql
from work.mylib.redis_my import MyRedis

from work.mylib.lib import delete_special_characters, contain_number, sentence_length, delete_extra_spaces
from work.mylib.lib import delete_url_link, delete_brackets_content, delete_brackets, replace_newline_characters
from work.dingding.dingding_decorator import dingding_monitor
from work.Englisht.deal_apostrophe import apostrophe_index


class ProcessNews(object):
    def __init__(self):
        pass

    def read_data(self):
        file_name = r"C:\Users\Administrator\Desktop\work_temp\英语句子扩量\article.txt"
        with open(file_name, 'r', encoding='utf8')as f:
            for line in f:
                data = json.loads(line.strip())
                yield data.get("url"), data.get("content")

    def process_data(self):
        with open('chinadaily_news_sentence.txt', 'a', encoding='utf8') as s_f, \
                open('chinadaily_news_num_sentence.txt', 'a', encoding='utf8') as n_f:

            for item in self.read_data():
                url, content = item
                if "chinadaily" in url:
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

                # 区分来源
                # if "chinadaily" in content:
                #     pass
                # elif "articles" in content:
                #     pass  # google新闻
                # elif "thejakartapost" in content:
                #     pass
                # elif "ehainan" in content:
                #     pass
                # elif "eguizhou" in content:
                #     pass
                # elif "ehangzhou" in content:
                #     pass
                # elif "nationthailand" in content:
                #     pass
                # elif "exploringtianjin" in content:
                #     pass
                # elif "english.snd" in content:
                #     pass

    @dingding_monitor
    def remove_repeat_sentence(self):
        """
            去重
        :return:
        """
        mr = MyRedis()

        remove_before_file = "news_sentence_temp.txt"
        remove_after_file = "news_sentence_new.txt"

        with open(remove_before_file, 'r', encoding='utf8')as f, \
                open(remove_after_file, 'a', encoding='utf8') as new_f:

            for line in f:
                sentence = line.strip()
                fingerprint = mr.generate_md5(sentence)
                if not mr.hash_exist(fingerprint):
                    new_f.write(sentence + "\n")
                    mr.hash_(fingerprint)
                else:
                    print(sentence)

    @dingding_monitor
    def same_sentence(self):
        """
            输出到文件
        :return:
        """
        from work.mylib.lib import big_file_remove_same
        big_file_remove_same("chinadaily_news_num_sentence.txt", "chinadaily_news_num_sentence_temp.txt")
        big_file_remove_same("chinadaily_news_sentence.txt", "chinadaily_news_sentence_temp.txt")

    def count(self):
        num = 0
        with open(r'BBC_news_sentence_temp.txt', 'r', encoding='utf8') as f:
            for line in f:
                num += 1
        print(num)


if __name__ == '__main__':
    pn = ProcessNews()
    pn.process_data()
    pn.same_sentence()
