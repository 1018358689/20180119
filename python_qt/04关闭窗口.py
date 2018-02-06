#!/usr/bin/env python
# -*- coding:utf-8 -*-

#QPushButton(string text, QWidget parent = None)
#text参数是将显示在按钮中的内容。
#parent参数是一个用来放置我们按钮的组件。在我们的例子中将会是QWidget组件。一个应用的组件是分层结构的。在这个分层内，大多数组件都有父类。没有父类的组件是顶级窗口。

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtCore import (QCoreApplication, QObject)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)  #quit 不是quit()
        qbtn.setToolTip('quit')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('退出')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xp = Example()
    sys.exit(app.exec_())

