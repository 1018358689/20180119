#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 一个参数传的是父类，第二个参数是title，第三个参数显示文本内容，第四个参数是按钮的集合，第五个参数是默认选中哪个按钮。
# 最后的event.accept(),表示允许处理这个事件，也就是执行关闭操作.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('啦啦啦啦')
        self.show()
    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,'标题','内容',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
            print('1')
        else:
            QCloseEvent.ignore()
            print('2')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xp = Example()
    sys.exit(app.exec_())
