from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QHBoxLayout, QApplication,
)
from qfluentwidgets import ComboBox, PrimaryToolButton, FluentIcon, LineEdit, CaptionLabel, SimpleCardWidget, \
    PrimaryPushButton, SpinBox, RoundMenu, Action, InfoBar, InfoBarPosition, DoubleSpinBox

from src.gui.icon.Icon import Icon
from src.utils.Config import cfg
from src.utils.CoordinatePicker import CoordinatePicker



class MouseMoveItem(SimpleCardWidget):

    class MouseMoveAttributeItem(SimpleCardWidget):
        def __init__(self, parent_mouse_widget_item):
            super().__init__(parent_mouse_widget_item)
            self.parent_mouse_widget_item = parent_mouse_widget_item
            layout = QVBoxLayout(self)
            # 添加编辑X和Y坐标的LineEdits
            self.x_edit = LineEdit()
            layout.addWidget(CaptionLabel("X坐标:"))
            layout.addWidget(self.x_edit)

            self.y_edit = LineEdit()
            layout.addWidget(CaptionLabel("Y坐标:"))
            layout.addWidget(self.y_edit)
            #添加撑开布局
            layout.addStretch(1)

            #点击次数输入框
            self.click_times_edit = DoubleSpinBox()
            layout.addWidget(CaptionLabel("移动时间:"))
            layout.addWidget(self.click_times_edit)
            #确认按钮
            self.confirm_button = PrimaryPushButton(FluentIcon.ACCEPT,"确认设置")
            self.confirm_button.clicked.connect(self.confirm_click)
            layout.addWidget(self.confirm_button)
            self.init_data()

        # 初始化数据
        def init_data(self):
            try:
                #使用父类的对应值
                self.x_edit.setText(self.parent_mouse_widget_item.x_value_label.text())
                self.y_edit.setText(self.parent_mouse_widget_item.y_value_label.text())
                self.click_times_edit.setValue(self.parent_mouse_widget_item.duration.value())
            except Exception as e:
                print(e)
        def confirm_click(self):
            try:
                # 获取输入的坐标值
                x = int(self.x_edit.text())
                y = int(self.y_edit.text())

                # 获取点击次数
                duration = self.click_times_edit.value()
                # 获取父类的对应值
                self.parent_mouse_widget_item.x_value_label.setText(str(x))
                self.parent_mouse_widget_item.y_value_label.setText(str(y))
                self.parent_mouse_widget_item.duration.setValue(duration)
            except Exception as e:
                print(e)

    def __init__(self, icon_path=None):
        super().__init__()
        # 创建主水平布局
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)
        # 左侧：拾取坐标按钮
        pick_button = PrimaryToolButton(Icon('move').icon)
        pick_button.setToolTip("拾取页面坐标")
        pick_button.setToolTipDuration(1000)
        pick_button.clicked.connect(self.pick_coordinates)
        main_layout.addWidget(pick_button)
        # 中部：坐标值显示及下拉选框
        center_layout = QHBoxLayout()
        main_layout.addLayout(center_layout)
        # 坐标值显示
        coordinates_layout = QHBoxLayout()
        x_label = CaptionLabel("X:")
        self.x_value_label = LineEdit()
        #设置默认值
        self.x_value_label.setText("0")
        y_label = CaptionLabel("Y:")
        self.y_value_label = LineEdit()
        # 设置默认值
        self.y_value_label.setText("0")
        coordinates_layout.addWidget(x_label)
        coordinates_layout.addWidget(self.x_value_label)
        coordinates_layout.addWidget(y_label)
        coordinates_layout.addWidget(self.y_value_label)
        center_layout.addLayout(coordinates_layout)

        #中间使用水平Spacer撑开
        main_layout.addStretch(1)
        self.duration = DoubleSpinBox()
        main_layout.addWidget(CaptionLabel("移动时间:"))
        main_layout.addWidget(self.duration)
        #监听数值改变
        self.listeningChanged()



#控件坐标拾取功能
    def pick_coordinates(self):
        #最小化窗口
        # 获取应用程序实例
        app = QApplication.instance()
        # 获取应用程序的主窗口
        self.main_window = app.activeWindow()
        #将主窗口最小化
        self.main_window.setWindowState(Qt.WindowMinimized)

        self.pick_window = CoordinatePicker()
        self.pick_window.show()
        self.pick_window.coordinate_picked_signal.connect(self.set_coordinates)

    #设置坐标
    def set_coordinates(self, coordinates):
        try:
            x,y = coordinates
            self.x_value_label.setText(str(x))
            self.y_value_label.setText(str(y))
            # 将主窗口最大化
            self.main_window.setWindowState(Qt.WindowMaximized)
        except Exception as e:
            print(e)

    #获取属性子类
    def get_attribute_widget_class(self):
        self.atribute_widget = self.MouseMoveAttributeItem(self)
        return self.atribute_widget

    #拖动创建序列化信息
    def init_attribute_dict(self,index):
        try:
            value =  {
                "index":index,
                "name":"鼠标移动",
                "type":"MouseMoveItem",
                "properties":{
                    "x": "0",
                    "y": "0",
                    "duration": "0"
                },
                "method": "mouse_move"
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
                self.x_value_label.setText(data["actions"][i]["properties"]["x"])
                self.y_value_label.setText(data["actions"][i]["properties"]["y"])
                self.duration.setValue(float(data["actions"][i]["properties"]["duration"]))
                print("移动控件数据初始化成功")
    #记录索引信息
    def setindex(self,index):
        self.index = index

    #为所有属性配置信号槽
    def listeningChanged(self):
        self.x_value_label.textChanged.connect(self.valueChanged)
        self.y_value_label.textChanged.connect(self.valueChanged)
        self.duration.valueChanged.connect(self.valueChanged)

    #监听数值更新
    def valueChanged(self):
        #直接更新所有值
        try:
            x = int(self.x_value_label.text())
            y = int(self.y_value_label.text())
            duration =float(self.duration.text())
            print("数值改变",x,y,duration)
            #将数值更新到序列化信息中
            data = cfg.get(cfg.projectData)
            for i in range(len(data["actions"])):
                if data["actions"][i]["index"] == self.index:
                    data["actions"][i]["properties"]["x"] = str(x)
                    data["actions"][i]["properties"]["y"] = str(y)
                    data["actions"][i]["properties"]["duration"] = str(duration)
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
                content="删除了一个移动 操作节点！✅",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self.parentWidget()
            )

        except Exception as e:
            print(e)






