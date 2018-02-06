#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QToolTip, QPushButton)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Tip：QWidget')
        btn = QPushButton('按钮', self)
        btn.setToolTip('Tip:Button')
        btn.resize(btn.sizeHint())
        btn.setGeometry(100,100,300,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
