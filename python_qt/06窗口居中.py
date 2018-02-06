#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 通过QDesktopWidget().availableGeometry().center()获得当前电脑屏幕的中心点。然后让widget的Geometry也改变中心点。之后self.move(qr.topLeft())就可以了。
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,30,300,200)
        self.center()
        self.show()
    def center(self):
        qr = self.frameGeometry() #获得Widget的坐标和大小
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xp = Example()
    sys.exit(app.exec_())
