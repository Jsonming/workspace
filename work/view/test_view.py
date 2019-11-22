#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import sys
import time
import requests
import datetime
import os
import re
import json
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from lxml import etree

tparms = {'filedir': ''}


class MyBrowser(QWidget):

    def __init__(self, parent=None):
        super(MyBrowser, self).__init__(parent)
        self.setWindowTitle(u"查询软件5.0")
        self.setStyleSheet("background-color:#FFFFFF;")
        self.setWindowIcon(QtGui.QIcon(self.resource_path('logo.png')))
        self.resize(984, 730)
        self.setFixedSize(350, 600)

        tparms['product_list'] = [{'a': 'a'}]
        self.jianshu_count = 1
        self.js_urllist = []
        # self.product_id = tparms['product_list'][0].values()[0]
        self.product_id = "a"
        self.js_spider_state = False
        self.zh_spider_state = False
        self.file_dir = tparms['filedir']
        self.createLayout()
        self.createConnection()

    def createLayout(self):
        self.all_title = QtGui.QPushButton(u"文章自动采集")
        self.all_title.setStyleSheet("background-color: #5bb05d;color:#fff;border-radius:5px;")
        self.all_title.setFixedSize(120, 40)

        product_label = QtGui.QLabel(u"       产品")
        product_label.setStyleSheet("background-color:#42a6fe;color:#fff;border-radius:5px;")
        product_label.setFixedHeight(40)
        product_label.setFixedWidth(120)

        self.product_label_text = QtGui.QComboBox()
        self.product_label_text.setStyleSheet(
            "background-color: #f2f4fe;border: 1px solid white;border-bottom:1px solid #DBDBDB;padding:2px 8px;")
        self.product_label_text.setFixedHeight(40)
        self.product_label_text.setFixedWidth(120)
        self.product_label_text.addItems(["a"])

        keyword_label = QtGui.QLabel(u"       关键词")
        keyword_label.setStyleSheet("background-color:#42a6fe;color:#fff;border-radius:5px;")
        keyword_label.setFixedHeight(40)
        keyword_label.setFixedWidth(120)

        self.keyword_label_text = QLineEdit()
        self.keyword_label_text.setStyleSheet("background-color:#f2f4fe;border-radius:5px;")
        self.keyword_label_text.setFixedHeight(40)
        self.keyword_label_text.setFixedWidth(120)

        already_result = QtGui.QLabel(u"  已查询文章：")
        already_result.setStyleSheet("background-color:#42a6fe;color:#fff;border-radius:5px;")
        already_result.setFixedHeight(40)
        already_result.setFixedWidth(120)

        self.already_result_count = QtGui.QLabel(u"0")
        self.already_result_count.setStyleSheet("background-color:#f2f4fe;border-radius:5px;")
        self.already_result_count.setFixedHeight(40)
        self.already_result_count.setFixedWidth(120)

        layout_left_top4 = QtGui.QHBoxLayout()
        layout_left_top4.addWidget(already_result)
        layout_left_top4.addWidget(self.already_result_count)

        layout_left_top = QtGui.QHBoxLayout()
        layout_left_top.addWidget(keyword_label)
        layout_left_top.addWidget(self.keyword_label_text)

        layout_left_top2 = QtGui.QHBoxLayout()
        layout_left_top2.addWidget(product_label)
        layout_left_top2.addWidget(self.product_label_text)

        self.start_button = QtGui.QPushButton(QtGui.QIcon(""), u"开始", self)
        self.start_button.setStyleSheet("background-color: #42a6fe;color:#fff;border-radius:5px;")
        self.start_button.setFixedSize(120, 40)

        self.upload_button = QtGui.QPushButton(QtGui.QIcon(""), u"结果", self)
        self.upload_button.setStyleSheet("background-color: #42a6fe;color:#fff;border-radius:5px;")
        self.upload_button.setFixedSize(120, 40)

        layout_left_top3 = QtGui.QHBoxLayout()
        layout_left_top3.addWidget(self.start_button)
        layout_left_top3.addWidget(self.upload_button)

        self.quit_out = QtGui.QPushButton(QtGui.QIcon(""), u"退出", self)
        self.quit_out.setStyleSheet("background-color: #42a6fe;color:#fff;border-radius:5px;")
        self.quit_out.setFixedSize(120, 40)

        self.show_url = QtGui.QTextBrowser()
        self.show_url.setStyleSheet(
            "color:#484848;gridline-color: #cbdcf1;background-color: #fff;alternate-background-color: #cbdcf1;selection-color: white;selection-background-color: #cbdcf1;border: 0.5px groove #cbdcf1;border-radius: 5px;padding: 2px 4px;")
        self.show_url.setOpenExternalLinks(True)

        self._page = QWebPage()
        self._view = QWebView()
        self._page.userAgentForUrl = self.user_agent
        self._view.setPage(self._page)
        self._view.page().userAgentForUrl = self.user_agent

        self.js_page = QWebPage()
        self.js_view = QWebView()
        self.js_page.userAgentForUrl = self.user_agent
        self.js_view.setPage(self.js_page)

        self.tt_page = QWebPage()
        self.tt_view = QWebView()
        self.tt_page.userAgentForUrl = self.user_agent
        self.tt_view.setPage(self.tt_page)

        Layout_left = QVBoxLayout()
        Layout_left.addWidget(self.all_title)
        Layout_left.addLayout(layout_left_top)
        Layout_left.addLayout(layout_left_top2)
        Layout_left.addLayout(layout_left_top3)
        Layout_left.addLayout(layout_left_top4)
        Layout_left.addWidget(self.quit_out)

        Layout_right = QVBoxLayout()
        Layout_right.addWidget(self.show_url)

        Layout_main = QtGui.QHBoxLayout()
        Layout_main.addLayout(Layout_left)
        # Layout_main.addLayout(Layout_right)

        self.setLayout(Layout_main)
        self.show()

    def resource_path(self, relative):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative)
        return os.path.join(relative)

    def createConnection(self):
        self.start_button.clicked.connect(self.allstart)
        self.product_label_text.currentIndexChanged.connect(self.selectionchange)
        self.quit_out.clicked.connect(self.close)
        self.upload_button.clicked.connect(self.get_res_jianshu)

    def selectionchange(self, change):
        self.product_id = tparms['product_list'][int(change)].values()[0]

    def allstart(self):
        keyword = self.keyword_label_text.text()
        if keyword == '':
            QtGui.QMessageBox.critical(self, u'错误', u'请输入搜索关键词')
        else:
            self.js_urllist = []
            self.final_proid = self.product_id
            self.start_button.setDisabled(True)
            self.product_label_text.setDisabled(True)
            self.start_button.setText(u"开始获取")
            self.start_button.setStyleSheet("background-color: #d44e4d;color:#fff;border-radius:5px;")
            tparms['js_key'] = keyword
            self.search_jianshu(keyword)

    def search_jianshu(self, keyword):
        url = 'https://www.jianshu.com/search?q={}&page={}&type=note'.format(keyword, self.jianshu_count)
        self.js_view.load(QUrl(url))
        self.jianshu_count += 1

    def get_res_jianshu(self):
        self.js_parse()
        self.search_jianshu(tparms['js_key'])

    def js_parse(self):
        res = self.js_view.page().mainFrame().toHtml()
        resp = res.data()
        document = etree.HTML(resp)
        try:
            urls = document.xpath('//div[@class="content"]/a')
            for url in urls:
                rurl = 'https://www.jianshu.com' + url.attrib['href']
                print(rurl)
        except Exception as e:
            print(str(e))

    def user_agent(self, param):
        return 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = MyBrowser()
    browser.show()
    sys.exit(app.exec_())
    browser.close()
