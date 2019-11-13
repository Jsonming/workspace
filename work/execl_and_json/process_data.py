#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 16:21
# @Author  : yangmingming
# @Site    : 
# @File    : process_data.py
# @Software: PyCharm
import json


class process_data(object):
    def __init__(self):
        pass

    def read_data(self, file_path):
        with open(file_path, 'r', encoding='utf8')as f:
            data = json.load(f)
        return data

    def process_data(self, data):
        data_megs = data.get("data")
        with open('result.txt', 'a', encoding='utf8')as f:
            for meg in data_megs:
                parentId = meg.get("parentId")
                if parentId == "2A180DA4-5170-210A-9E91-6C3B4678EAE2":
                    id = meg.get("id")
                    name = meg.get("name")
                    f.write(name + '\n')
                    for m in data_megs:
                        if m.get("pId") == id:
                            f.write("     " + m.get("name") + '\n')
                    f.write("\n")


if __name__ == '__main__':
    pd = process_data()

    file_path = 'data.json'
    data = pd.read_data(file_path)
    pd.process_data(data)
