from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QAction
#导入QIcon
from PyQt5.QtGui import QIcon
from src.gui.main_ui import Main_Ui
from qfluentwidgets import Action
from qfluentwidgets import FluentIcon as FIF

class MainInterface(QWidget,Main_Ui):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.HeaderToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.HeaderToolBar.addActions([
            Action(FIF.ADD,self.tr('add')),
            Action(FIF.DELETE,self.tr('delete'))
        ])


