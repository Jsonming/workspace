#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import hashlib
import shutil

def getmd5(file):
    if not os.path.isfile(file):
        return
    fd = open(file,'rb')
    md5 = hashlib.md5()
    md5.update(fd.read())
    fd.close()
    return md5.hexdigest()

if __name__ == "__main__":
    allfile = []
    md5list = []
    identicallist = []

    start = time.time()
    input_path = "E:\\code\\abnormal"
    input_dir = os.listdir(input_path)
    for path in input_dir:
        inpath=input_path+"\\"+path
        temp_path = inpath+"\\temp"
        uipath = str(inpath)

        for path,dir,filelist in os.walk(uipath):
            for filename in filelist:
                pic=os.path.join(path, filename)
                allfile.append(os.path.join(path,filename))

    #根据MD5值比较
    for photo in allfile:
        md5sum = getmd5(photo)
        if md5sum not in md5list:
            md5list.append(md5sum)
        else:
            identicallist.append(photo)


    end = time.time()
    last = end - start
    print(identicallist)
    for path in identicallist:
        shutil.move(path,temp_path)
    print("identical photos: " + str(len(identicallist)))
    print("time: " + str(last) +"s")
    print("count: " + str(len(allfile)))



