#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 17:19
# @Author  : yangmingming
# @Site    : 
# @File    : pyhdfs_learn.py
# @Software: PyCharm

import pyhdfs

import pyhdfs


class PackageHdfs(object):
    """
        此类是python 调用hadoop 的hdfs类，也是采用python调的方式，非常方便。
        包封装的也是hdfs shell 是一样的功能也可以采用 os.system（）函数执行 hdfs shell, 不利于批量
        此类封装，利于python 程序调用。
    """

    def __init__(self):
        self.fs = pyhdfs.HdfsClient('192.168.200.19:9870', user_name="hadoop")  # 用户名一定要写上

    def makdir(self, filePath):
        """
        新建目录, 判断文件是否存在如果，不存在则创建
        :param filePath:
        :return:
        """
        fs = self.fs
        if not fs.exists(filePath):
            fs.mkdirs(filePath)

    def delFile(self, path):
        """
        删除
        :param path:
        :return:
        """
        fs = self.fs
        fs.delete(path)

    def upload(self, fileName, tmpFile):
        """
            上传文件
        :param fileName:
        :param tmpFile:
        :return:
        """
        fs = self.fs
        fs.copy_from_local(fileName, tmpFile)

    def rename(self, srcPath, dstPath):
        """
            重命名
        :param srcPath:
        :param dstPath:
        :return:
        """
        fs = self.fs
        if not fs.exists(srcPath):
            return
        fs.rename(srcPath, dstPath)


if __name__ == '__main__':
    pg_hdfs = PackageHdfs()
    pg_hdfs.makdir()