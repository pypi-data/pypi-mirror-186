from PyQtGuiLib.header import (
    PYQT_VERSIONS,
    QApplication,
    sys,
    QWidget,
    qt,
    QPushButton,
    Qt,
    QPalette,
    QColor,
    QPaintEvent,
    QPainter,
    QBrush,
    QSize,
    QPropertyAnimation
)

'''
    测试用例的标准模板,该代码用于复制
'''
from PyQt5.QtGui import QBitmap
from PyQt5.QtWidgets import QGraphicsOpacityEffect

class Test(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(600,600)

        # self.setAttribute(qt.WA_TranslucentBackground)
        # self.setWindowFlags(qt.FramelessWindowHint | qt.Widget)

        self.st = QPushButton("开始覆盖背景",self)
        self.st.move(200,200)
        self.st.clicked.connect(self.st_e)


        # self.btn = QPushButton("测试",self)
        self.w1 = QWidget(self)
        self.w1.move(10,10)
        self.w1.resize(0,0)
        self.w1.setStyleSheet("background-color: rgb(0, 0, 0,255);")

        self.w2 = QWidget(self)
        self.w2.move(10,10)
        self.w2.resize(150,150)
        self.w2.setStyleSheet("background-color: rgb(255, 252, 171,100);")

        self.btn = QPushButton("测试",self.w2)
        self.btn.resize(60,30)
        self.btn.move(30,30)
        self.btn.setStyleSheet('''
background-color:transparent;
border:1px solid rgb(0, 0, 0);
        ''')

        self.ani = QPropertyAnimation(self.w1,b"size")
        self.ani.setStartValue(self.w1.size())
        self.ani.setEndValue(QSize(150,150))
        self.ani.setDuration(1500)
        self.ani.finished.connect(self.end_e)


    def end_e(self):
        self.btn.setStyleSheet('''
        background-color:transparent;
        border:1px solid rgb(255, 255, 255);
        color:rgb(255, 255, 255)
                ''')

    def st_e(self):
        self.ani.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Test()
    win.show()

    if PYQT_VERSIONS in ["PyQt6","PySide6"]:
        sys.exit(app.exec())
    else:
        sys.exit(app.exec_())