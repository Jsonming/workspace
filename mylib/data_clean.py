#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/16 11:06
# @Author  : yangmingming
# @Site    : 
# @File    : data_clean.py
# @Software: PyCharm
import re
from mylib.language_identification import recognition_language


class DataClean(object):
    def __init__(self):
        self.pattern_url = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        self.pattern_url_two = re.compile(r'www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

        self.pattern_html = re.compile(r'<.*?>')
        self.pattern_script = re.compile("<script[^>]*>([\\S\\s]*?)<\/script>", re.IGNORECASE)
        self.pattern_style = re.compile("<style[^>]*>([\\S\\s]*?)<\/style>", re.I)

        self.re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
        self.re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
        self.re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
        self.re_br = re.compile('<br\s*?/?>')  # 处理换行
        self.re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        self.re_comment = re.compile('<!--[^>]*-->')  # HTML注释

        self.special_charater = re.compile(
            "♪|=|※|●|■|~|▶|▲|▼|☞|►|▷|◇|○|Ⓞ|°|¤|▫|#|◆|⚽|♬|[①②③④⑤⑥⑦⑧]+|×|™|@►|▻|～|⁺|⋆|℃|℉|-")

    def read_file_data(self, file):
        """
            读取文件数据， 返回一个生成器，用以应对文件比较大的情况
        :param file: 文件名
        :return: 生成器
        """
        with open(file, 'r', encoding='utf8')as f:
            for line in f:
                yield line

    def clean_url(self, content):
        """
            清除文本中的链接
        :return:
        """
        content = re.sub(self.pattern_url, ' ', content)
        content = re.sub(self.pattern_url_two, ' ', content)

        return content

    def replaceCharEntity(self, htmlstr):
        CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                         'lt': '<', '60': '<',
                         'gt': '>', '62': '>',
                         'amp': '&', '38': '&',
                         'quot': '"', '34': '"', }

        re_charEntity = re.compile(r'&#?(?P<name>\w+);')
        sz = re_charEntity.search(htmlstr)
        while sz:
            entity = sz.group()  # entity全称，如&gt;
            key = sz.group('name')  # 去除&;后entity,如&gt;为gt
            try:
                htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
            except KeyError:
                # 以空串代替
                htmlstr = re_charEntity.sub('', htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
        return htmlstr

    def clean_html(self, content):
        """
            清除文本中的HTML标签和html命名实体
        :param content:
        :return:
        """
        content = re.sub(self.pattern_script, ' ', content)
        content = re.sub(self.pattern_style, ' ', content)
        content = re.sub(self.pattern_html, ' ', content)

        s = self.re_cdata.sub('', content)  # 去掉CDATA
        s = self.re_script.sub('', s)  # 去掉SCRIPT
        s = self.re_style.sub('', s)  # 去掉style
        s = self.re_br.sub('\n', s)  # 将br转换为换行
        s = self.re_h.sub('', s)  # 去掉HTML 标签
        s = self.re_comment.sub('', s)  # 去掉HTML注释
        blank_line = re.compile('\n+')  # 去掉多余的空行
        s = blank_line.sub('\n', s)
        s = self.replaceCharEntity(s)  # 替换实体
        return s

    def clean_special_character(self, content):
        """
            清除特殊字符
        :param content:
        :return:
        """
        return re.sub(self.special_charater, '', content)

    def clean_word(self, content):
        """
            清除掉没有意义的单词
        :param content:
        :return:
        """
        word = ['Login', 'download', 'registry']
        patt_word = "(" + "|".join(word) + ")"
        return re.sub(patt_word, '', content)

    def clean_code(self, content):
        """
            删除文本中的代码段，
        :param content:
        :return:
        """
        result = []
        lines = content.split('\n')
        for line in lines:
            if line.startswith('...'):
                line = line[3:]
            elif line.startswith('..'):
                line = line[2:]
            elif line.startswith('.') or line.startswith(','):
                line = line[1:]

            if 'Dialogue' in line:
                result.append(line.split(',')[9])
            else:
                result.append(line)
        return '\n'.join(result)

    def clean_language(self, content):
        """
            删除文本中非本国语言的情况
        :param contetn:
        :return:
        """
    def clean_blank(self, content):
        return re.sub('[\s]+', ' ', content)

    def run(self):
        """数据清洗控制逻辑"""
        # 需要清洗的文件 file
        file = r"C:\Users\Administrator\Desktop\vietnam_speaking.txt"
        new_file = r"C:\Users\Administrator\Desktop\temp.txt"
        data = self.read_file_data(file)
        for line in data:
            content = self.clean_url(line.strip())
            content = self.clean_html(content)
            content = self.clean_special_character(content)
            content = self.clean_word(content)
            content = self.clean_blank(content)
            content = self.clean_code(content)
            content = content.strip()
            if recognition_language(content) == "越南语":
                with open(new_file, 'a', encoding='utf8')as ff:
                    ff.write(content + "\n")


if __name__ == '__main__':
    clean = DataClean()
    clean.run()
