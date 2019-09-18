#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 18:39
# @Author  : yangmingming
# @Site    : 
# @File    : remove_img.py
# @Software: PyCharm
import os
from mylib.lib import list_file, move_file


def judge_by_name():
    first_folder = r"I:\work\OCR\vietnam\4"
    second_folder = r"I:\work\OCR\vietnam\5"

    old_files = list_file(first_folder)
    _old_files = [f.split('\\')[-1] for f in old_files]
    new_files = list_file(second_folder)

    for file in new_files:
        file_name = file.split("\\")[-1]
        if file_name in _old_files:
            try:
                move_file(file, r"I:\work\OCR\vietnam\temp")
            except Exception as e:
                os.remove(file)


judge_by_name()
