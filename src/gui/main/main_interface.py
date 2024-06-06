import ast
import os
import shutil
import time

from PyQt5.QtCore import Qt, QMimeData, QByteArray, QEvent
from PyQt5.QtGui import QDrag, QDropEvent
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QAbstractItemView, QListWidgetItem, QApplication, QInputDialog
#导入QIcon
from pip._vendor import requests

from src.gui.main.main_ui import Main_Ui
from qfluentwidgets import Action, json, InfoBar, InfoBarPosition
from qfluentwidgets import FluentIcon as FIF
from src.gui.main import UploadMessageBox

#引入全部方法
from src.automation.methods import *

from src.gui.icon.Icon import Icon

from src.automation.actions import *

from src.utils.Config import cfg


class MainInterface(QWidget,Main_Ui):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        #设置菜单栏
        self.HeaderToolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.HeaderToolBar.addActions([
            Action(FIF.SAVE,self.tr('保存')),
            Action(FIF.PLAY,self.tr('运行')),
            Action(FIF.CLOUD,self.tr('上传'))
        ])

        #设置动作列表树
        self.setactiontree()
        #设置拖放相关配置
        self.dragdrop()

        #保存菜单绑定方法
        self.HeaderToolBar.actions()[0].triggered.connect(self.save)
        #运行菜单绑定方法
        self.HeaderToolBar.actions()[1].triggered.connect(self.run)
        #上传菜单绑定方法
        self.HeaderToolBar.actions()[2].triggered.connect(self.upload)

        #设置谁被点击
        self.flag =""
        self.ActionList.itemPressed.connect(self.item_pressed_handler)

        #当控件被点击时，加载属性
        self.VisualizationList.itemClicked.connect(self.load_attribute_widget)

        #设置控件字典
        self.setActionDict()
        #设置自动化方法
        self.set_automation_method()



    #设置拖放相关配置
    def dragdrop(self):
        self.VisualizationList.setDragDropMode(QAbstractItemView.DragDrop)
        # 设置可视化流程列表接受拖放
        self.VisualizationList.setAcceptDrops(True)
        self.VisualizationList.viewport().setAcceptDrops(True)
        self.VisualizationList.dropEvent = self.drop_event_handler

        # 设置动作栏允许拖拽
        self.ActionList.setDragEnabled(True)
        self.ActionList.dragDropMode = QAbstractItemView.InternalMove

    # 设置动作列表树
    def setactiontree(self):
        #设置动作列表树
        mouse_keyboard = QTreeWidgetItem(self.ActionList)

        mouse_keyboard.setText(0,self.tr('键鼠操作'))

        mouseclick = QTreeWidgetItem(mouse_keyboard)
        mouseclick.setText(0,self.tr('鼠标点击'))
        mouseclick.setIcon(0,Icon('mouse').icon)

        mousemove = QTreeWidgetItem(mouse_keyboard)
        mousemove.setText(0, self.tr('鼠标移动'))
        mousemove.setIcon(0, Icon('mouse').icon)

        mousedrag = QTreeWidgetItem(mouse_keyboard)
        mousedrag.setText(0, self.tr('鼠标拖拽'))
        mousedrag.setIcon(0, Icon('mouse').icon)

        mousescroll = QTreeWidgetItem(mouse_keyboard)
        mousescroll.setText(0, self.tr('鼠标滚动'))
        mousescroll.setIcon(0, Icon('mouse').icon)

        inputenglish = QTreeWidgetItem(mouse_keyboard)
        inputenglish.setText(0, self.tr('输入英文'))
        inputenglish.setIcon(0, Icon('shortcut').icon)

        inputchinese = QTreeWidgetItem(mouse_keyboard)
        inputchinese.setText(0, self.tr('输入中文'))
        inputchinese.setIcon(0, Icon('shortcut').icon)

        hotkey = QTreeWidgetItem(mouse_keyboard)
        hotkey.setText(0,self.tr('快捷键'))
        hotkey.setIcon(0,Icon('shortcut').icon)

        images = QTreeWidgetItem(self.ActionList)
        images.setText(0,self.tr('图片'))
        imageclick = QTreeWidgetItem(images)
        imageclick.setText(0,self.tr('图像点击'))
        imageclick.setIcon(0,Icon('imgicon').icon)




    def item_pressed_handler(self, item: QTreeWidgetItem, column: int):
        print(item.text(0))
        self.flag = item.text(0)

    def drop_event_handler(self, event: QDropEvent):
        if self.flag != "":
            try:
                custom_item = self.AUTOMATION.get(self.flag)
                custom_item = custom_item()
            except Exception as e:
                print(e)
            try:
                list_item = QListWidgetItem(self.VisualizationList)
                self.VisualizationList.setItemWidget(list_item, custom_item)
                list_item.setSizeHint(custom_item.sizeHint())
                #设置当前元素索引
                index = self.VisualizationList.count()-1
                custom_item.init_attribute_dict(index)
                event.acceptProposedAction()
            except Exception as e:
                print(e)

    #加载属性配置页面
    def load_attribute_widget(self, list_item):
        try:
            #清空 AttributeList 原有的子节点
            while self.AttributeList.count() > 0:
                self.AttributeList.takeItem(0)

            custom_widget = list_item.listWidget().itemWidget(list_item)
            attribute_widget_class = custom_widget.get_attribute_widget_class()
            # attribute_widget = attribute_widget_class()
            attribute_widget = attribute_widget_class
            list_item = QListWidgetItem(self.AttributeList)
            self.AttributeList.setItemWidget(list_item, attribute_widget)
            list_item.setSizeHint(attribute_widget.sizeHint())
        except Exception as e:
            print(e)

    #可视化列表初始化
    def initVisualizationList(self):
        try:
            #先清空列表
            while self.VisualizationList.count() > 0:
                self.VisualizationList.takeItem(0)
            loaddata = cfg.get(cfg.projectData)
            # 转换为字典
            # loaddata = json.loads(loaddata)
            print("数据:",loaddata)
            for action in loaddata['actions']:
                custom_item = self.AUTOMATION.get(action['name'])
                custom_item = custom_item()

                list_item = QListWidgetItem(self.VisualizationList)
                self.VisualizationList.setItemWidget(list_item, custom_item)
                list_item.setSizeHint(custom_item.sizeHint())
                #设置当前元素索引
                index = self.VisualizationList.count()-1
                custom_item.setindex(index)
                #初始化数据
                custom_item.initialisation()

            formatted_json = json.dumps(loaddata, indent=4)
            self.SourceCodeEdit.setPlainText(formatted_json)
        except Exception as e:
            print(e)

    #保存流程的方法
    def save(self):
        try:
            # 项目根目录
            folder_path = cfg.get(cfg.projectFolder)
            data = cfg.get(cfg.projectData)
            print("数据:",data['actions'])
            project_name = data["project_name"]
            # 当前项目目录
            project_path = folder_path + '/' + data["project_name"]
            #将 data 转换为json数据 写入 project_name 同名的json文件下
            with open(project_path + '/' + project_name + '.json', 'w',encoding='utf-8') as f:
                json.dump(data, f,ensure_ascii=False, indent=4)
                InfoBar.success(
                    title='保存成功',
                    content="项目 [" + project_name + "] 已保存👀",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self
                )
                formatted_json = json.dumps(data, indent=4)
                self.SourceCodeEdit.setPlainText(formatted_json)
                print("保存成功")
        except Exception as e:
            print(e)

    #运行流程的方法
    def run(self):
        try:
            #先保存再运行流程
            self.save()
            # 获取项目根目录
            folder_path = cfg.get(cfg.projectFolder)
            # 获取项目数据
            data = cfg.get(cfg.projectData)
            # 获取项目名
            project_name = data["project_name"]
            # 获取项目目录
            project_path = folder_path + '/' + data["project_name"]
            # 获取项目json文件
            json_file = project_path + '/' + project_name + '.json'
            # 获取项目json文件内容
            with open(json_file, 'r',encoding='utf-8') as f:
                data = json.load(f)
            actions = data['actions']
            print("actions:",actions)

            #最小化主窗口
            app = QApplication.instance()
            main_window = app.activeWindow()
            main_window.setWindowState(Qt.WindowMinimized)
            #延时
            time.sleep(1)
            #遍历执行方法 method 的 value 对应执行的方法 properties是填入方法的参数
            for action in actions:
                method = action['method']
                properties = action['properties']
                print("method:",method)
                print("properties:",properties)
                #执行方法
                automethod = self.AUTOMATION_METHOD.get(method)
                automethod(**properties)
            main_window.setWindowState(Qt.WindowMaximized)
            InfoBar.success(
                title='执行成功',
                content="流程成功执行完毕！🎈",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )

        except Exception as e:
            main_window.setWindowState(Qt.WindowMaximized)
            InfoBar.warning(
                title='失败',
                content="流程执行失败！🤡",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=-1,  # 永不消失
                parent=self
            )

            print(e)

    def setActionDict(self):
        self.AUTOMATION = {
            "鼠标点击": MouseClickItem,
            "鼠标移动": MouseMoveItem,
            "鼠标拖拽": MouseDragItem,
            "鼠标滚动": MouseScrollItem,
            "输入英文": InputEnglishItem,
            "输入中文": InputChineseItem,
            "快捷键": InputHotkeyItem,
            "图像点击": ImageClickItem



        }
    def set_automation_method(self):
        self.AUTOMATION_METHOD = {
            "mouse_click": mouse_click,
            "mouse_move": mouse_move,
            "mouse_drag": mouse_drag,
            "mouse_scroll": mouse_scroll,
            "input_english": input_english,
            "input_chinese": input_chinese,
            "input_hotkey": input_hotkey,
            "click_image": click_image,
        }

    def upload(self):
        try:
            #获取服务端地址
            server_host = cfg.get(cfg.serverHost)
            # 弹出widget 输入用户名密码
            mesage_box = UploadMessageBox(self)
            if mesage_box.exec():
                username = mesage_box.usernameLineEdit.text()
                password = mesage_box.passwordLineEdit.text()
                note = mesage_box.noteLineEdit.text()
                #将项目文件夹压缩为zip文件上传
                folder_path = cfg.get(cfg.projectFolder)
                project_name = cfg.get(cfg.projectData)["project_name"]
                if os.path.exists(folder_path + '/' + project_name):
                    zip_file = folder_path + '/' + project_name
                    shutil.make_archive(zip_file, 'zip', folder_path + '/' + project_name)
                    print("项目压缩成功")

                #向flask后端发送请求
                response = requests.post(
                    server_host + '/upload/',
                    data={'username': username, 'password': password,'note': note},
                    files={'file': open(zip_file + '.zip', 'rb')})


                #发起请求
                if response.status_code == 200:
                    InfoBar.success(
                        title='上传成功',
                        content="项目 [" + project_name + "] 已上传至服务器👀",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=2000,
                        parent=self
                    )
                else:
                    InfoBar.warning(
                        title='上传失败',
                        content="项目 [" +project_name + "] 上传失败！🤡",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.BOTTOM,
                        duration=-1,  # 永不消失
                        parent=self
                    )
                # 删除zip文件
                os.remove(zip_file + '.zip')
                print("项目压缩删除成功")



        except Exception as e:
            print(e)













