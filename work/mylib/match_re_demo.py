#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 18:22
# @Author  : yangmingming
# @Site    : 
# @File    : match_re_demo.py
# @Software: PyCharm
import re

s = u"""我是一个人（中国人）aaa[真的]bbbb{确定}【ys】21我‘’是一'个人'(中国""人dfsd“”)a[a]a[真的]bbbb{确定} ] //       / /   ?    헤커 박의 조언은 단순하고s}{d][fad(sda><sdf) 명확'\'전전 궁금'\'은 퍽퍽한 살림살이에 하다"""

pattern_one = re.compile("♪|=|※|●|■|~|▶|▲|▼|☞|►|★|▷|◇|-|…|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+|×|&|™|@►|▻|～|⁺|⋆|’|℃|℉", re.S)
pattern_two = re.compile(r"""\(|\)|{|}|<|>|\[|\]|（|）|"|【|】|『|』|'|“|”|‘|’|,|;|；|:|'|∼|\.""")
pattern_three = re.compile("[a-zA-Z0-9]+", re.S)
pattern_four = re.compile("[\u4e00-\u9fa5]+", re.S)  # 中文
pattern_five = re.compile("[\uac00-\ud7ff]+", re.S)  # 韩语
pattern_six = re.compile("[\u30a0-\u30ff]+|[\u3040-\u309f]+", re.S)  # 日文
pattern_seven = re.compile(u"[\u3000-\u303f\ufb00-\ufffd]+")  # 标点符号
pattern_eight = re.compile("\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\(.*?\\)|\\{.*?}|\\[.*?]|<.*?>", re.S)
pattern_nine = re.compile("[\u0060|\u0021-\u002c|\u002e-\u002f|\u003a-\u003f|\u2200-\u22ff|\uFB00-\uFFFD|\u2E80-\u33FF]")

a = set(re.findall(pattern_nine, s))
p = set(""";,-!.?"'""")

# a = re.sub(pattern_eight, '', s)
# print(a)

print(p)