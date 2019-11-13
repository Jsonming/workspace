#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 13:54
# @Author  : yangmingming
# @Site    : 
# @File    : data_dudplication.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from work.mylib import NewProcess
from work.mylib import gen_md5


class DataDeduplication(object):
    def __init__(self):
        pass

    def read_data(self, file):
        with open(file, 'r', encoding='utf8')as f:
            data = f.readlines()
            data = [item.strip() for item in data]
        return data

    def remove_same(self, data):
        return list(set(data))

    def read_execl(self, file):
        """ 读execl"""
        try:
            data = pd.read_excel(file, sheet_name="content")
        except:
            try:
                data = pd.read_excel(file, sheet_name="Sheet1")
            except:
                try:
                    data = pd.read_excel(file, sheet_name="news_content")
                except:
                    data = pd.read_excel(file, sheet_name="data")

        data = np.array(data).tolist()
        data = [item[0] for item in data]
        return data

    def run(self):
        """ 主逻辑控制"""
        # 新抓的批数据
        file = r"C:\Users\Administrator\Desktop\vietnam\新闻\thannien.vn.txt"
        data = self.read_data(file)
        data = self.remove_same(data)

        # show data

        # #前一批数据
        data_two = []

        # 文件夹中是execl 打开这个
        # folder = r"C:\Users\Administrator\Desktop\Viet-news"
        # for file_a in os.listdir(folder):
        #     file_name = os.path.join(folder, file_a)
        #     data_ = self.read_execl(file_name)
        #     data_two.extend(data_)
        #
        # 文件夹中是txt 打开这个
        # folder = r"C:\Users\Administrator\Desktop\temp"
        # for file_a in os.listdir(folder):
        #     file_name = os.path.join(folder, file_a)
        #     print(file_name)
        #     old_data = self.read_data(file_name)
        #     data_two.extend(old_data)

        # 以前数据只有一个文件，打开这个
        # old_file = r"C:\Users\Administrator\Desktop\vietnam_speaking_sentence_new.txt"
        # old_data = self.read_data(old_file)
        # old_data = self.remove_same(old_data)
        # data_two.extend(old_data)
        # print('前数据条数：', len(data_two))

        # 与前一批数据去重后的新数据

        new_data = list(set(data) - set(data_two))
        print('新数据条数：', len(data))
        print('前批数据条数：', len(data_two))
        print('去重后数据条数：', len(new_data))

        # #存储去重后数据
        new_data = data
        new = NewProcess()
        new.save_txt(r"C:\Users\Administrator\Desktop\vietnam_news\kenh14.vn.txt", new_data)
        # char_sum = sum([len(item.split()) for item in new_data])
        # print("平均句子长度", char_sum / len(new_data))

    def file_remove_same(self):
        """
            run 函数应对数据量级比较小的去重，大数量级去重应该使用此方法
        :return:
        """
        finger_print = set()
        input_file = r"C:\Users\Administrator\Desktop\vietnam\新闻\www.vnexpress.net.txt"
        output_file = r"C:\Users\Administrator\Desktop\vietnam_news\www.vnexpress.net.txt"
        with open(input_file, 'r', encoding='utf8') as f, open(output_file, 'w', encoding='utf8') as ff:
            for line in f:
                line_string = line.strip()
                finger = gen_md5(line_string)
                if finger not in finger_print:
                    finger_print.add(finger)
                    ff.write(line)


if __name__ == '__main__':
    dd = DataDeduplication()
    dd.file_remove_same()
