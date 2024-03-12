# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF


class HorizontalCommandBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.setStyleSheet('background: white')  # 设置背景色

        # 创建并添加一系列Action到布局中
        actions = [
            Action(FIF.COPY, 'Copy'),
            Action(FIF.CUT, 'Cut'),
            Action(FIF.PASTE, 'Paste'),
            Action(FIF.SETTING, 'Settings'),
            Action(FIF.HELP, 'Help'),
            Action(FIF.FEEDBACK, 'Feedback'),
        ]

        for action in actions:
            button = RoundMenu(parent=self)
            button.addAction(action)
            button.setFixedSize(50, 50)  # 调整按钮大小以适应水平布局
            button.setGeometry(QRect(0, 0, 50, 50))  # 可能需要根据实际情况调整位置和尺寸
            button.setStyleSheet('border-radius: 25px;')  # 增大圆角使其更像圆形按钮
            self.layout.addWidget(button)

        # ... 其他配置和功能实现


class Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Command Bar Demo")
        self.resize(400, 300)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        self.command_bar = HorizontalCommandBar()
        layout.addWidget(self.command_bar)

        central_widget = QWidget(self)
        layout.addWidget(central_widget)
        layout.setStretch(1, 1)  # 确保内容区域填充剩余空间

        inner_layout = QHBoxLayout(central_widget)
        inner_layout.setAlignment(Qt.AlignCenter)
        label = QLabel('This is the main content area', self)
        inner_layout.addWidget(label)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()