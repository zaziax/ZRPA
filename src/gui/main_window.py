from qfluentwidgets import SplitFluentWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QHBoxLayout, QLabel
from qfluentwidgets import RoundMenu, setTheme, Theme, Action, MenuAnimationType, MenuItemDelegate, CheckableMenu, MenuIndicatorType
from qfluentwidgets import FluentIcon as FIF

class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-RPA")
