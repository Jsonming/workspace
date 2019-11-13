#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 14:18
# @Author  : yangmingming
# @Site    : 
# @File    : movie_same_remove.py
# @Software: PyCharm
import os

from pymediainfo import MediaInfo

from work.mylib import list_file, move_file


class MovieSameRemove(object):
    """
        各种方法检查视频是否重复，
    """

    def __init__(self):
        self.folder = r"C:\Users\Administrator\Desktop\remove"  # 文件夹

    def judge_by_name(self):
        """
            利用
        :return:
        """
        first_folder = r"I:\work\OCR\vietnam\1"
        second_folder = r"I:\work\OCR\vietnam\5"

        old_files = os.listdir(first_folder)
        new_files = os.listdir(second_folder)

        for file in new_files:
            if file in old_files:
                move_file(second_folder + "\\" + file, second_folder + "\\temp")

    def judge_by_size(self):
        file_info = []
        for file in list_file(self.folder):
            media_info = MediaInfo.parse(file)
            data_info = media_info.to_data().get("tracks")[0]
            duration = data_info.get("duration")
            file_size = data_info.get("file_size")
            judge_info = (duration, file_size)
            if judge_info not in file_info:
                file_info.append(judge_info)
            else:
                move_file(file, self.folder + "\\temp")


if __name__ == '__main__':
    msr = MovieSameRemove()
    msr.judge_by_name()
