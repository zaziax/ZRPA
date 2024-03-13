from PyQt5.QtWidgets import QWidget

from src.gui.main_ui import Main_Ui

class MainInterface(QWidget,Main_Ui):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
