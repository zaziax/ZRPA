# from PyQt5.QtGui import QIcon, QPixmap
# from src.resources.img import rpa_rc
#
# class Icon:
#     def __init__(self, name, parent=None):
#         self.name = name
#         self.parent = parent
#         self.icon = QIcon()
#         self.icon.addPixmap(QPixmap(":/icon/"+name), QIcon.Normal, QIcon.Off)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from src.resources.img import rpa_rc


class Icon:
    def __init__(self, name, size=(64, 64), parent=None):
        self.name = name
        self.parent = parent
        self.icon = QIcon()

        # 加载原始图标
        pixmap = QPixmap(":/icon/" + name)

        # 缩放到指定大小
        scaled_pixmap = pixmap.scaled(size[0], size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.icon.addPixmap(scaled_pixmap, QIcon.Normal, QIcon.Off)
