#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 16:51
# @Author  : yangmingming
# @Site    : 
# @File    : theading_check.py
# @Software: PyCharm
from work.mylib.redis_my import SSDBCon
import time
from threading import Thread

mr = SSDBCon()
input_file = r"temp.txt"
output_file = "new.txt"

diff_db = ["corpus_ebook_fingerprint", "corpus_news_fingerprint", "corpus_recording_fingerprint",
           "corpus_translation_fingerprint", "corpus_speech_fingerprint"]

flag = []


def aaa(db_name, sentence):
    mr = SSDBCon()
    global flag
    flag.append(mr.exist_finger(db_name, sentence))


def bbb():
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
                print(sentence)
            flag = []


start = time.time()
bbb()
end = time.time()

print(end - start)
