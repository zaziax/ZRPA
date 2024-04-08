from qfluentwidgets import SplitFluentWindow
from qfluentwidgets import setTheme, Theme
from qfluentwidgets import FluentIcon as FIF

from src.gui.main.main_interface import MainInterface

class MainWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-RPA")
        setTheme(Theme.LIGHT)

        #添加子页面
        self.mainInterface = MainInterface(self)
        self.addSubInterface(self.mainInterface,FIF.ROBOT,'流程编辑')

        self.mainInterface2 = MainInterface(self)
        self.addSubInterface(self.mainInterface2,FIF.BOOK_SHELF,'流程管理')


