from qfluentwidgets import SplitFluentWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QHBoxLayout, QLabel
from qfluentwidgets import RoundMenu, setTheme, Theme, Action, MenuAnimationType, MenuItemDelegate, CheckableMenu, MenuIndicatorType
from qfluentwidgets import FluentIcon as FIF

from src.gui.main_interface import MainInterface

class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-RPA")

        #添加子页面
        self.mainInterface = MainInterface(self)

        self.addSubInterface(self.mainInterface,FIF.ROBOT,'流程编辑')
