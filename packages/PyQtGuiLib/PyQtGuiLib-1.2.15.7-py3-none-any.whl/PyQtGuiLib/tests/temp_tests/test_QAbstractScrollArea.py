import sys

from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, QRect, QEasingCurve, QParallelAnimationGroup
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 500)

        self.setStyleSheet("QPushButton{border-radius:12px;"
                           "border:6px solid rgb(85, 255, 255);"
                           "background-color:rgb(255, 255, 255);"
                           "font: 20px \"MiSans\"}")

        self.btn = QPushButton("改变颜色", self)
        self.btn.resize(200, 100)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.anim_group)

        self._my_color = QColor()
        self._frame_geometry = QRect()

        self._my_color = QColor(0, 0, 0)

    @pyqtProperty(QRect)
    def frame_geometry(self):
        return self._frame_geometry

    @frame_geometry.setter
    def frame_geometry(self, value):
        self._frame_geometry = value
        self.upd_btn()

    @pyqtProperty(QColor)
    def my_color(self):
        return self._my_color

    @my_color.setter
    def my_color(self, value):
        self._my_color = value

    def upd_btn(self):
        red, green, blue = self._my_color.red(), self._my_color.green(), self._my_color.blue()
        self.btn.setGeometry(self._frame_geometry)
        self.btn.setStyleSheet(f"background-color: rgb({red}, {green}, {blue});"
                               f"border:6px solid rgb({green}, {blue}, {red});"
                               f"color: rgb({blue}, {red}, {green});")

    def anim_group(self):

        self.anim_col = QPropertyAnimation(self, b"my_color")
        self.anim_col.setDuration(1000)
        self.anim_col.setStartValue(QColor(255, 0, 127))
        self.anim_col.setEndValue(QColor(0, 255, 127))
        self.anim_col.setEasingCurve(QEasingCurve.Type.OutQuad)

        self.anim_geom = QPropertyAnimation(self, b"frame_geometry")
        self.anim_geom.setStartValue(QRect(200, 200, 200, 100))
        self.anim_geom.setEndValue(QRect(400, 200, 400, 100))
        self.anim_geom.setDuration(1000)
        self.anim_geom.setEasingCurve(QEasingCurve.Type.OutQuad)

        anim = QParallelAnimationGroup(self)
        anim.addAnimation(self.anim_col)
        anim.addAnimation(self.anim_geom)
        anim.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test()
    win.show()
    sys.exit(app.exec())