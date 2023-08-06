# -*- coding:utf-8 -*-
# @time:2023/1/1522:25
# @author:LX
# @file:45.py
# @software:PyCharm
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQtGuiLib.core import BubbleWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("气泡测试")
        self.resize(1000, 600)

        self.btn = QPushButton("测试", self)
        self.btn.resize(130, 100)
        self.btn.move(200, 200)

        self.btn.enterEvent = self.b_show
        self.btn.leaveEvent = self.b_hide

    def b_show(self, e):
        self.b = BubbleWidget(self)
        self.b.resize(100, 30)
        self.b.setBColor(QColor(0, 0, 0))
        # self.b.setDurationTime(BubbleWidget.Be_Forever)
        self.b.setDurationTime(3)
        # self.b.setAnimationEnabled(True)
        # self.b.setDurationTime(3)
        self.b.setDirection(BubbleWidget.Down)
        self.b.setText("这是一个气泡")
        self.b.setTextSize(9)
        self.b.setTextColor(QColor(255, 170, 255))
        self.b.setKm(40, 10, 1)
        self.b.setTrack(self.btn)
        self.b.show()
        # self.b.finished.connect(self.b_hide)

    def b_hide(self):
        print("Dsa")
    #     self.b.hide()
    #     self.b.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
