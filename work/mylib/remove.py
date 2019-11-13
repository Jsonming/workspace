#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import hashlib
import shutil


def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file, 'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()


if __name__ == "__main__":
    all_file = []
    md5_list = []
    identical_list = []

    start = time.time()
    input_path = "E:\\code\\abnormal"
    input_dir = os.listdir(input_path)
    for path in input_dir:
        inpath = input_path + "\\" + path
        temp_path = inpath + "\\temp"
        uipath = str(inpath)

        for path, dir, filelist in os.walk(uipath):
            for filename in filelist:
                pic = os.path.join(path, filename)
                all_file.append(os.path.join(path, filename))

    # 根据MD5值比较
    for photo in all_file:
        md5sum = getmd5(photo)
        if md5sum not in md5_list:
            md5_list.append(md5sum)
        else:
            identical_list.append(photo)

    end = time.time()
    last = end - start
    print(identical_list)
    for path in identical_list:
        shutil.move(path, temp_path)
    print("identical photos: " + str(len(identical_list)))
    print("time: " + str(last) + "s")
    print("count: " + str(len(all_file)))
