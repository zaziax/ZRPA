from PyQt5.QtCore import Qt, QMimeData, QByteArray
from PyQt5.QtGui import QDrag, QDropEvent
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QAbstractItemView, QListWidgetItem
#导入QIcon
from src.gui.main.main_ui import Main_Ui
from qfluentwidgets import Action
from qfluentwidgets import FluentIcon as FIF

from src.gui.icon.Icon import Icon

from src.automation.actions import MouseWidgetItem,ShortCutWidgetItem


class MainInterface(QWidget,Main_Ui):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        #设置菜单栏
        self.HeaderToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.HeaderToolBar.addActions([
            Action(FIF.ADD,self.tr('新建')),
            Action(FIF.SAVE,self.tr('保存')),
            Action(FIF.PLAY,self.tr('运行')),
            Action(FIF.CLOUD,self.tr('上传'))
        ])

        #设置动作列表树
        self.setactiontree()

        # 设置可视化列表接受拖放
        self.VisualizationList.setAcceptDrops(True)
        self.VisualizationList.viewport().setAcceptDrops(True)
        self.VisualizationList.dropEvent = self.drop_event_handler

        # 设置ActionList允许拖拽
        self.ActionList.setDragEnabled(True)
        self.ActionList.dragDropMode = QAbstractItemView.InternalMove

        self.flag =""
        self.ActionList.itemPressed.connect(self.item_pressed_handler)

    # 设置动作列表树
    def setactiontree(self):
        #设置动作列表树
        mouse_keyboard = QTreeWidgetItem(self.ActionList)

        mouse_keyboard.setText(0,self.tr('键鼠操作'))
        mouse = QTreeWidgetItem(mouse_keyboard)
        mouse.setText(0,self.tr('鼠标'))
        mouse.setIcon(0,Icon('mouse').icon)

        shortcut = QTreeWidgetItem(mouse_keyboard)
        shortcut.setText(0,self.tr('快捷键'))
        shortcut.setIcon(0,Icon('shortcut').icon)

    def item_pressed_handler(self, item: QTreeWidgetItem, column: int):
        print(item.text(0))
        self.flag = item.text(0)

    def drop_event_handler(self, event: QDropEvent):
        if self.flag != "":
            if self.flag == self.tr('鼠标'):
                custom_item = MouseWidgetItem()  # 确保CoordinateWidgetItem正确实现
            elif self.flag == self.tr('快捷键'):
                custom_item = ShortCutWidgetItem()  # 示例代码，根据实际情况修改
            else:
                pass
            list_item = QListWidgetItem(self.VisualizationList)
            self.VisualizationList.setItemWidget(list_item, custom_item)
            list_item.setSizeHint(custom_item.sizeHint())
            event.acceptProposedAction()













