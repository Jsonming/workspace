#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 11:09
# @Author  : yangmingming
# @Site    : 
# @File    : json_to_execl.py
# @Software: PyCharm
import json
import pandas as pd


class JsonToExecl(object):
    def __init__(self):
        pass

    def read_data(self, file_path):
        with open(file_path, 'r', encoding='utf8') as f:
            return json.load(f)

    def trans_data(self, data):
        df = pd.DataFrame()
        for key, value in data.items():
            print(type(value))


if __name__ == '__main__':
    file_path = r"data.json"

    jte = JsonToExecl()
    data = jte.read_data(file_path)
    jte.trans_data(data)
