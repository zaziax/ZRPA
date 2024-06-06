from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QHBoxLayout, QApplication, QCompleter,
)
from qfluentwidgets import ComboBox, PrimaryToolButton, FluentIcon, LineEdit, CaptionLabel, SimpleCardWidget, \
    PrimaryPushButton, SpinBox, RoundMenu, Action, InfoBar, InfoBarPosition

from src.gui.icon.Icon import Icon
from src.utils.Config import cfg
from src.utils.CoordinatePicker import CoordinatePicker
import pyautogui as auto


class InputHotkeyItem(SimpleCardWidget):
    class InputHotkeyAttributeItem(SimpleCardWidget):
        def __init__(self, parent_mouse_widget_item):
            super().__init__(parent_mouse_widget_item)
            self.parent_mouse_widget_item = parent_mouse_widget_item
            layout = QVBoxLayout(self)

            self.hotkeya = LineEdit()
            layout.addWidget(CaptionLabel("按键1:"))
            layout.addWidget(self.hotkeya)

            self.hotkeyb = LineEdit()
            layout.addWidget(CaptionLabel("按键2:"))
            layout.addWidget(self.hotkeyb)

            self.hotkeyc = LineEdit()
            layout.addWidget(CaptionLabel("按键3:"))
            layout.addWidget(self.hotkeyc)

            #确认按钮
            self.confirm_button = PrimaryPushButton(FluentIcon.ACCEPT,"确认设置")
            self.confirm_button.clicked.connect(self.confirm_click)
            layout.addWidget(self.confirm_button)
            self.init_data()

        # 初始化数据
        def init_data(self):
            try:
                #使用父类的对应值
                self.hotkeya.setText(self.parent_mouse_widget_item.hotkeya.text())
                self.hotkeyb.setText(self.parent_mouse_widget_item.hotkeyb.text())
                self.hotkeyc.setText(self.parent_mouse_widget_item.hotkeyc.text())

            except Exception as e:
                print(e)
        def confirm_click(self):
            try:
                hotkeya = self.hotkeya.text()
                hotkeyb = self.hotkeyb.text()
                hotkeyc = self.hotkeyc.text()
                # 获取父类的对应值
                self.parent_mouse_widget_item.hotkeya.setText(hotkeya)
                self.parent_mouse_widget_item.hotkeyb.setText(hotkeyb)
                self.parent_mouse_widget_item.hotkeyc.setText(hotkeyc)

            except Exception as e:
                print(e)

    def __init__(self, icon_path=None):
        super().__init__()
        # 创建主水平布局
        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)
        # 左侧：拾取坐标按钮
        pick_button = PrimaryToolButton(Icon('hotkey').icon)
        pick_button.setToolTip("快捷键输入")
        pick_button.setToolTipDuration(1000)
        main_layout.addWidget(pick_button)


        self.hotkeya = LineEdit()
        main_layout.addWidget(CaptionLabel("按键1:"))
        main_layout.addWidget(self.hotkeya)
        self.hotkeya.setText("")

        self.hotkeyb = LineEdit()
        main_layout.addWidget(CaptionLabel("按键2:"))
        main_layout.addWidget(self.hotkeyb)
        self.hotkeyb.setText("")

        self.hotkeyc = LineEdit()
        main_layout.addWidget(CaptionLabel("按键3:"))
        main_layout.addWidget(self.hotkeyc)
        self.hotkeyc.setText("")


        #监听数值改变
        self.listeningChanged()

        #设置补全
        self.completion()


    #获取属性子类
    def get_attribute_widget_class(self):
        self.atribute_widget = self.InputHotkeyAttributeItem(self)
        return self.atribute_widget

    #拖动创建序列化信息
    def init_attribute_dict(self,index):
        try:
            value =  {
                "index":index,
                "name":"快捷键",
                "type":"InputHotkeyItem",
                "properties":{
                    "hotkeya": "",
                    "hotkeyb": "",
                    "hotkeyc": ""
                },
                "method": "input_hotkey"
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
        try:
            #获取序列化信息
            data = cfg.get(cfg.projectData)
            #获取当前索引
            self.index
            #获取当前索引对应的序列化信息
            for i in range(len(data["actions"])):
                if data["actions"][i]["index"] == self.index:
                    self.hotkeya.setText(data["actions"][i]["properties"]["hotkeya"])
                    self.hotkeyb.setText(data["actions"][i]["properties"]["hotkeyb"])
                    self.hotkeyc.setText(data["actions"][i]["properties"]["hotkeyc"])
                    print("快捷键控件数据初始化成功")
        except Exception as e:
            print(e)

    #记录索引信息
    def setindex(self,index):
        self.index = index

    #为所有属性配置信号槽
    def listeningChanged(self):
        self.hotkeya.textChanged.connect(self.valueChanged)
        self.hotkeyb.textChanged.connect(self.valueChanged)
        self.hotkeyc.textChanged.connect(self.valueChanged)

    #监听数值更新
    def valueChanged(self):
        #直接更新所有值
        try:
            hotkeya = self.hotkeya.text()
            hotkeyb = self.hotkeyb.text()
            hotkeyc = self.hotkeyc.text()

            print("数值改变",hotkeya,hotkeyb,hotkeyc)
            #将数值更新到序列化信息中
            data = cfg.get(cfg.projectData)
            for i in range(len(data["actions"])):
                if data["actions"][i]["index"] == self.index:
                    if hotkeya != "":
                        data["actions"][i]["properties"]["hotkeya"] = hotkeya
                    if hotkeyb != "":
                        data["actions"][i]["properties"]["hotkeyb"] = hotkeyb
                    if hotkeyc != "":
                        data["actions"][i]["properties"]["hotkeyc"] = hotkeyc
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
                content="删除了一个快捷键操作节点！✅",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self.parentWidget()
            )

        except Exception as e:
            print(e)

    def  completion(self):
        stans = [
                '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\',
                ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt',
                'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward',
                'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert',
                'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc',
                'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19',
                'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn',
                'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1',
                'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9',
                'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print',
                'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select',
                'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'stop', 'subtract', 'tab', 'up',
                'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option',
                'optionleft', 'optionright'
                ]
        completera = QCompleter(stans,self.hotkeya)
        completera.setCaseSensitivity(Qt.CaseInsensitive)
        completera.setMaxVisibleItems(10)
        self.hotkeya.setCompleter(completera)

        completerb = QCompleter(stans, self.hotkeyb)
        completerb.setCaseSensitivity(Qt.CaseInsensitive)
        completerb.setMaxVisibleItems(10)
        self.hotkeyb.setCompleter(completerb)

        completerc = QCompleter(stans, self.hotkeyc)
        completerc.setCaseSensitivity(Qt.CaseInsensitive)
        completerc.setMaxVisibleItems(10)
        self.hotkeyc.setCompleter(completerc)








