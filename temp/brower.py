#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


class MyBrowser(QWidget):
    def __init__(self, parent=None):
        super(MyBrowser, self).__init__(parent)
        self.createLayout()
        self.createConnection()

    def search(self):
        res = self._view.page().mainFrame().toHtml()
        resp = res.toUtf8().data()
        print resp
        # address = str(self.addressBar.text())
        # if address:
        #     if address.find('://') == -1:
        #         address = 'http://' + address
        #     url = QUrl(address)
        #     self._view.load(url)

    def createLayout(self):
        self.setWindowTitle("focus browser")

        self.addressBar = QLineEdit()
        self.goButton = QPushButton("Search")

        bl = QHBoxLayout()
        bl.addWidget(self.addressBar)
        bl.addWidget(self.goButton)

        self._page = QWebPage()
        self._view = QWebView()
        self._view.setPage(self._page)
        self._window = QMainWindow()
        self._window.setCentralWidget(self._view)
        a = QString.fromUtf8('https://www.jianshu.com/search?q=护栏&page=2&type=note')
        url = QUrl(a)
        self._view.load(url)
        layout = QVBoxLayout()
        layout.addLayout(bl)
        layout.addWidget(self._window)

        self.setLayout(layout)

    def createConnection(self):
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.search)
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.goButton, SIGNAL('clicked()'), self.search)
        self.connect(self.goButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))


 if __name__ == '__main__':
    app = QApplication(sys.argv)

    browser = MyBrowser()
    browser.show()

    sys.exit(app.exec_())