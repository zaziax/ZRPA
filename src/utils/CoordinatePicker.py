

import time
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
import pyautogui as auto


class CoordinatePicker(QWidget):
    coordinate_picked_signal = pyqtSignal(tuple)  # 定义一个信号，用于发送坐标值

    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_mouse_position)
        self.timer.start(50)  # 设置适当的刷新频率，例如每20毫秒刷新一次

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, QApplication.desktop().width(), QApplication.desktop().height())

        # 提示信息标签
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setStyleSheet("background-color: rgba(41, 241, 255, 0.1);")
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setText("点击鼠标左键获取坐标")
        self.label.setCursor(QCursor(Qt.CrossCursor))

        self.coord_label = QLabel(self)
        self.coord_label.setStyleSheet("color: white; font-size: 14px; border: 1px solid white; padding: 2px;")
        self.coord_label.setAlignment(Qt.AlignCenter)
        self.update_mouse_position()  # 初始化坐标标签的位置

    def update_mouse_position(self):
        x,y = auto.position()
        cursor_pos = QCursor.pos()
        self.coord_label.setText(f"X: {x}, Y: {y}")
        self.coord_label.move(cursor_pos.x()+5, cursor_pos.y()+5)
        # self.coord_label.move(x, y)  # 在鼠标位置旁边显示

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = auto.position()
            # cursor_pos = event.globalPos()
            print(f"Clicked at coordinates: X={x}, Y={y}")
            self.coordinate_picked_signal.emit((x, y))  # 发送坐标值
            self.close()








