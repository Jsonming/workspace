#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 22:31
# @Author  : yangmingming
# @Site    : 
# @File    : hashlib_learn.py
# @Software: PyCharm

import hashlib
string = "hello world "
string2 = "hello python "
m1 = hashlib.md5()
m1.update(string.encode('utf8'))
print(m1.hexdigest())
m1.update(string2.encode('utf8'))
print(m1.hexdigest())

m2 = hashlib.md5()
string3 = string + string2
m2.update(string3.encode('utf8'))
print(m2.hexdigest())


# m2 = hashlib.sha1()
# m3 = hashlib.sha256()
h = hashlib.new('ripemd160')
h.update("Nobody inspects the spammish repetition".encode("utf8"))
