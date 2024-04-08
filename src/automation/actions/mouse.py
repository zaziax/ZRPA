import sys
from PyQt5.QtWidgets import (
    QApplication, QListWidget, QListWidgetItem, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QIcon

class MouseWidgetItem(QWidget):
    def __init__(self, icon_path=None):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        # 图标
        if icon_path:
            self.icon_label = QLabel()
            pixmap = QIcon(icon_path).pixmap(24, 24)
            self.icon_label.setPixmap(pixmap)
            self.layout.addWidget(self.   icon_label)

        # 拾取坐标按钮
        self.pick_button = QPushButton("Pick Coordinates")
        self.pick_button.clicked.connect(self.pick_coordinates)
        self.layout.addWidget(self.pick_button)

        # 坐标值显示
        self.coordinates_layout = QHBoxLayout()
        self.x_label = QLabel("X:")
        self.x_value_label = QLabel("0")
        self.y_label = QLabel("Y:")
        self.y_value_label = QLabel("0")
        self.coordinates_layout.addWidget(self.x_label)
        self.coordinates_layout.addWidget(self.x_value_label)
        self.coordinates_layout.addWidget(self.y_label)
        self.coordinates_layout.addWidget(self.y_value_label)
        self.layout.addLayout(self.coordinates_layout)

    def pick_coordinates(self):
        # 这里模拟获取坐标，实际应用中应替换为真实获取坐标的方法
        x, y = 100, 200
        self.x_value_label.setText(str(x))
        self.y_value_label.setText(str(y))

