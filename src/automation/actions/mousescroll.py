from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QHBoxLayout, QApplication,
)
from qfluentwidgets import ComboBox, PrimaryToolButton, FluentIcon, LineEdit, CaptionLabel, SimpleCardWidget, \
    PrimaryPushButton, SpinBox, RoundMenu, Action, InfoBar, InfoBarPosition

from src.gui.icon.Icon import Icon
from src.utils.Config import cfg
from src.utils.CoordinatePicker import CoordinatePicker
import pyautogui as auto


class MouseScrollItem(SimpleCardWidget):

    class MouseScrollAttributeItem(SimpleCardWidget):
        def __init__(self, parent_mouse_widget_item):
            super().__init__(parent_mouse_widget_item)
            self.parent_mouse_widget_item = parent_mouse_widget_item
            layout = QVBoxLayout(self)
            # 添加编辑X和Y坐标的LineEdits
            self.nums = LineEdit()
            layout.addWidget(CaptionLabel("滚动量:"))
            layout.addWidget(self.nums)

            #确认按钮
            self.confirm_button = PrimaryPushButton(FluentIcon.ACCEPT,"确认设置")
            self.confirm_button.clicked.connect(self.confirm_click)
            layout.addWidget(self.confirm_button)
            self.init_data()

        # 初始化数据
        def init_data(self):
            try:
                #使用父类的对应值
                self.nums.setText(self.parent_mouse_widget_item.nums.text())

            except Exception as e:
                print(e)
        def confirm_click(self):
            try:
                # 获取输入的坐标值
                nums = self.nums.text()
                # 获取父类的对应值
                self.parent_mouse_widget_item.nums.setText(nums)

            except Exception as e:
                print(e)

    def __init__(self, icon_path=None):
        super().__init__()
        # 创建主水平布局
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)
        # 左侧：拾取坐标按钮
        pick_button = PrimaryToolButton(Icon('click').icon)
        pick_button.setToolTip("滚动")
        pick_button.setToolTipDuration(1000)
        main_layout.addWidget(pick_button)
        #中间使用水平Spacer撑开
        main_layout.addStretch(1)
        #下拉选框2设置点击次数
        self.nums = LineEdit()
        main_layout.addWidget(CaptionLabel("滚动数值:"))
        main_layout.addWidget(self.nums)
        #监听数值改变
        self.listeningChanged()


    #获取属性子类
    def get_attribute_widget_class(self):
        self.atribute_widget = self.MouseScrollAttributeItem(self)
        return self.atribute_widget

    #拖动创建序列化信息
    def init_attribute_dict(self,index):
        try:
            value =  {
                "index":index,
                "name":"鼠标滚动",
                "type":"MouseScrollItem",
                "properties":{
                    "nums": "0"
                },
                "method": "mouse_scroll"
            }
            print("索引信息", index)
            print(value)
            self.index = index
            projectdata = cfg.get(cfg.projectData)
            projectdata["actions"].append(value)
            cfg.set(cfg.projectData, projectdata)
            print(cfg.projectData)
        except Exception as e:
            print(e)

    #从序列化信息加载时数据初始化
    def initialisation(self):
        #获取序列化信息
        data = cfg.get(cfg.projectData)
        #获取当前索引
        self.index
        #获取当前索引对应的序列化信息
        for i in range(len(data["actions"])):
            if data["actions"][i]["index"] == self.index:
                self.nums.setText(data["actions"][i]["properties"]["nums"])
                print("点击控件数据初始化成功")
    #记录索引信息
    def setindex(self,index):
        self.index = index

    #为所有属性配置信号槽
    def listeningChanged(self):
        self.nums.textChanged.connect(self.valueChanged)

    #监听数值更新
    def valueChanged(self):
        #直接更新所有值
        try:
            nums = self.nums.text()
            print("数值改变",nums)
            #将数值更新到序列化信息中
            data = cfg.get(cfg.projectData)
            for i in range(len(data["actions"])):
                if data["actions"][i]["index"] == self.index:
                    data["actions"][i]["properties"]["nums"] = nums
                    cfg.set(cfg.projectData, data)
                    print("更新序列化信息",data)

        except Exception as e:
            print(e)

    #右键弹出菜单
    def contextMenuEvent(self, event):
        menu = RoundMenu(self)
        menu.addAction(Action(FluentIcon.DELETE,"删除"))
        menu.exec(event.globalPos())
        event.accept()
        #删除被单击执行方法
        menu.triggered.connect(lambda action:self.remove())

    def remove(self):
        try:
            projectdata = cfg.get(cfg.projectData)
            for i in range(len(projectdata["actions"])):
                if projectdata["actions"][i]["index"] == self.index:
                    projectdata["actions"].pop(i)
                    cfg.set(cfg.projectData, projectdata)
                    print("删除序列化信息", projectdata)
                    break
            #后续索引值更新从头重新排序
            for i in range(len(projectdata["actions"])):
                projectdata["actions"][i]["index"] = i
                cfg.set(cfg.projectData, projectdata)
            print("更新后的序列化信息", projectdata)
            #移除指定索引的节点
            print("移除指定索引的节点",self.index)
            self.parentWidget().parentWidget().takeItem(self.index)

            #刷新列表
            # # 获取应用程序实例
            # app = QApplication.instance()
            # # 获取应用程序的主窗口
            # main_window = app.activeWindow()
            # main_window.mainInterface.initVisualizationList()

            InfoBar.success(
                title='删除节点成功',
                content="删除了一个滚动操作节点！✅",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self.parentWidget()
            )

        except Exception as e:
            print(e)






