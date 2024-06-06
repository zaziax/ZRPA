import os
from datetime import time, datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import PushButton, InfoBar, InfoBarPosition, json

from src.gui.projects.projects_ui import Projects_Ui

from src.gui.projects import MessageBox,ProjectItem
from src.utils.Config import cfg


class ProjectsInterface(QWidget,Projects_Ui):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loadProject()
        #为项目创建按钮绑定点击事件
        self.item.clicked.connect(self.create_project)

    #创建项目的方法
    def create_project(self):
        messageBox = MessageBox(self)
        if messageBox.exec():
            # 创建一个用于显示项目名称的正方形状按钮
            self.projectnew_label =ProjectItem()
            self.projectnew_label.set_item_text(messageBox.urlLineEdit.text())

            self.layout.addWidget(self.projectnew_label)
            #本地创建同名文件夹
            #项目根目录
            try:
                folder_path = cfg.get(cfg.projectFolder)
                # print(folder_path)
                #项目目录
                project_path = folder_path + "/" + messageBox.urlLineEdit.text()
                #创建 project_path 文件夹
                if not os.path.exists(project_path):
                    os.mkdir(project_path)
                # project_path 下创建同名.json 文件,创建img 文件夹
                try:
                    #创建.json 文件
                    with open(project_path + "/" + messageBox.urlLineEdit.text() + ".json", "w", encoding="utf-8") as f:
                        f.write("")

                    #创建img 文件夹
                    os.mkdir(project_path + "/img")

                    jsondata = {
                        "project_name": messageBox.urlLineEdit.text(),
                        "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "actions": []
                    }

                    # 写入json
                    with open(project_path + "/" + messageBox.urlLineEdit.text() + ".json", "w", encoding="utf-8") as f:
                        json.dump(jsondata,f,ensure_ascii=False,indent=4)

                        print("创建成功")

                    InfoBar.success(
                        title='创建成功',
                        content="项目 [" + messageBox.urlLineEdit.text() + "] 创建成功🎈",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP,
                        duration=2000,
                        parent=self
                    )
                except Exception as e:
                    print(e)
            except:
                pass

    #加载项目信息的方法
    def loadProject(self):
        folder_path = cfg.get(cfg.projectFolder)
        project_list=[]
        #遍历 folder_path 第一级文件夹名称获取项目
        # 获取根目录下的第一级子目录
        for dir in os.listdir(folder_path):
            if os.path.isdir(os.path.join(folder_path, dir)):  # 确保是目录而非文件
                project_list.append(dir)
        #遍历加载项目
        for project in project_list:
            self.project_label =ProjectItem()
            self.project_label.set_item_text(project)
            self.layout.addWidget(self.project_label)


