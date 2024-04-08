from PyQt5.QtGui import QIcon, QPixmap
from src.resources.img import rpa_rc

class Icon:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/icon/"+name), QIcon.Normal, QIcon.Off)
