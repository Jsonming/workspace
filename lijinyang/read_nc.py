#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 20:48
# @Author  : yangmingming
# @Site    : 
# @File    : read_nc.py
# @Software: PyCharm
import pandas as pd
from netCDF4 import Dataset


class Ncreader():
    def __init__(self):
        pass

    def read_nc_file(self, nc_file_path):
        nc_obj = Dataset(nc_file_path)
        return nc_obj

    def read_nc_var(self, nc_obj):
        keys = nc_obj.variables.keys()
        print(keys)
        return keys

    def nc_to_execl(self, nc_obj):
        nc_keys = self.read_nc_var(nc_obj)
        # lat = nc_obj.variables['lat'][:]
        # lon = nc_obj.variables['lon'][:]
        # time = nc_obj.variables['time'][:]
        # sst = nc_obj.variables['sst'][:]
        with open('soilw.txt', 'a', encoding='utf8') as f:
            for key in nc_keys:
                f.write(':'.join([key, str(list(nc_obj.variables[key][:]))]) + "\n")
        # for value in sst:
        #     print(value)


if __name__ == '__main__':
    nc_file_path = r'C:\Users\Administrator\Desktop\soilw.mon.mean.nc'

    nc_reader = Ncreader()
    nc_obj = nc_reader.read_nc_file(nc_file_path=nc_file_path)
    # nc_reader.read_nc_var(nc_obj)   # 查看变量
    nc_reader.nc_to_execl(nc_obj)
