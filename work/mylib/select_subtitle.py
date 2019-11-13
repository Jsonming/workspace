#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 15:08
# @Author  : yangmingming
# @Site    : 
# @File    : select_srt.py
# @Software: PyCharm
import chardet
from work.mylib import list_file
import os
import asstosrt


class SelectSubtitle(object):
    def __init__(self):
        """
            筛选字幕文件，字幕文件目前看大致三种，srt， ass, txt
        """

    def check_char(self, file_name):
        """
            查看文件的编码格式
        :param file_name: 文件名
        :return:
        """
        with open(file_name, 'rb')as f:
            data = f.read()

        return chardet.detect(data)

    def parse_srt(self, srt):
        """
            解析srt文件
        :param srt:  srt文件内容
        :return:
        """
        result = []
        for line in srt:
            line = line.strip()
            if len(line) and not line.isdigit():
                first_str = line[0:1]
                if not first_str.isdigit():
                    result.append(line)
                    # print(line)

        return '\n'.join(result)

    def parse_ass(self, ass):
        """
            解析ass 文件
        :param ass: ass 文件内容
        :return:
        """
        return ""

    def parse_txt(self, txt):
        """
            解析 txt 文件
        :param txt: txt 文件内容
        :return:
        """
        return ""

    def run(self, fold):
        """
            主要逻辑控制
        :param fold: 输入文件夹
        :return:
        """
        if os.path.isdir(fold):
            files = list_file(folder=fold)
        elif os.path.isfile(fold):
            files = [fold]
        else:
            print("不是文件夹不是文件, 你到底是啥")
            files = []
        for file in files:
            coding_msg = self.check_char(file)
            encoding_format = coding_msg.get("encoding")
            if encoding_format == "Windows-1254":
                encoding_format = "utf8"

            with open(file, 'r', encoding=encoding_format) as f:
                # if file.endswith("srt") or file.endswith('txt'):
                #     subtitle_content = self.parse_srt(f)
                # elif file.endswith("ass"):
                #     srt_str = asstosrt.convert(f)
                #     srt = srt_str.split('\n')

                # 如果是ass文件将ass文件转化为 srt格式，这次的txt内容上是srt文件所以不做区分
                if file.endswith("ass"):
                    srt_str = asstosrt.convert(f)
                    f = srt_str.split('\n')
                subtitle_content = self.parse_srt(f)

            with open(r'C:\Users\Administrator\Desktop\vietnam_speaking.txt', 'a', encoding='utf8') as f:
                f.write(subtitle_content + "\n")


if __name__ == '__main__':
    ss = SelectSubtitle()

    fold = r"C:\Users\Administrator\Desktop\vietnam_subtitle"
    # fold = r"C:\Users\Administrator\Desktop\vietnam_subtitle\%5BOFFICIAL%5D+CON+R_NG+CHAU+TIEN+2017+%7C+Phim+Ho_t+H峮h+Vi_t+t_+Biti's (1).srt"
    ss.run(fold)
