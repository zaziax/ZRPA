import os
import time
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QCursor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
import pyautogui as auto

from src.utils.Config import cfg


class Screenshot(QWidget):
    screenshot_taken_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_mouse_position)
        self.timer.start(50)  #
        self.start_pos = None
        self.end_pos = None

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, QApplication.desktop().width(), QApplication.desktop().height())

        # 提示信息标签
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setStyleSheet("background-color: rgba(41, 241, 255, 0.01);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setCursor(QCursor(Qt.CrossCursor))

        self.coord_label = QLabel(self)
        self.coord_label.setStyleSheet("color: white; font-size: 14px; border: 1px solid white; padding: 2px;")
        self.coord_label.setAlignment(Qt.AlignCenter)
        self.update_mouse_position()  # 初始化坐标标签的位置

    def update_mouse_position(self):
        x, y = auto.position()
        cursor_pos = QCursor.pos()
        self.coord_label.setText(f"X: {x}, Y: {y}")
        self.coord_label.move(cursor_pos.x() + 5, cursor_pos.y() + 5)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        painter.setPen(QPen(Qt.red, 2))
        painter.setBrush(Qt.NoBrush)  # 不使用画刷，保持透明
        if self.start_pos and self.end_pos:
            painter.drawRect(self.start_pos.x(), self.start_pos.y(), self.end_pos.x() - self.start_pos.x(),
                             self.end_pos.y() - self.start_pos.y())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.pos()
            self.end_pos = None
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_pos = event.pos()
            self.capture_screenshot()

    def capture_screenshot(self):
        try:

            # 获取截图范围
            left = min(self.start_pos.x(), self.end_pos.x())
            top = min(self.start_pos.y(), self.end_pos.y())
            width = abs(self.start_pos.x() - self.end_pos.x())
            height = abs(self.start_pos.y() - self.end_pos.y())

            # 转换窗口坐标为全局屏幕坐标
            window_rect = self.frameGeometry()
            screen_rect = QApplication.desktop().screenGeometry()
            left += window_rect.left() - screen_rect.left()
            top += window_rect.top() - screen_rect.top()

            rect_border = 2
            left += rect_border
            top += rect_border
            width -= rect_border * 2
            height -= rect_border * 2

            # 截取屏幕范围内的图片
            screenshot = QApplication.primaryScreen().grabWindow(0, left, top, width, height)

            #根项目目录
            path = cfg.get(cfg.projectFolder)
            data = cfg.get(cfg.projectData)
            #项目图片目录
            project_path =path+"/"+data["project_name"]+"/img"
            print("图片路径:",project_path)
            #生成
            # save_path = project_path+"/"+"RPA_"+int(time.time())+".png"
            # save_path = f"RPA_{int(time.time())}.png"
            save_path = os.path.join(project_path, f"RPA_{int(time.time())}.png")
            screenshot.save(save_path)
            self.screenshot_taken_signal.emit(save_path)  # 发送截图保存路径
            self.close()
        except Exception as e:
            print("Error capturing screenshot:", str(e))