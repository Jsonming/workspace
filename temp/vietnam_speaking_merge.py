#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 13:55
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_speaking_merge.py
# @Software: PyCharm
from work.mylib.data_dudplication import DataDeduplication
from work.mylib.mysql_my import MySql

file = r"C:\Users\Administrator\Desktop\vietnam_speaking.txt"

dd = DataDeduplication()
data = dd.read_data(file)
data = dd.remove_same(data)
print('新数据条数：', len(data))

my = MySql()
# show data
for line in data:
    print(line)
    values = (
        "https://vi.glosbe.com/zh/vi",
        line
    )

    sql = 'INSERT INTO {db_name}(url, content) VALUES(%s,%s)'.format(db_name="vietnam_speaking_sentence")  # 将表名设置为参数形式
    my.cursor.execute(sql, values)
    my.connect.commit()
