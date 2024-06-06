from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import PushButton, RoundMenu, Action, FluentIcon, FlowLayout, InfoBar, InfoBarPosition

from src.utils.Config import cfg


class ProjectItem(PushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setObjectName("project_label")

        self.setToolTipDuration(1000)
        # 设置按钮为正方形
        self.setFixedSize(150, 150)
        menu = RoundMenu(self)
        menu.addAction(Action(FluentIcon.DELETE,"删除"))

    def set_item_text(self,name):
        self.setText(name)
        self.setToolTip(name)

    def remove(self):
        try:
            layout_parent = self.parentWidget()
            layout_parent.layout.removeWidget(self)
            self.deleteLater()
            InfoBar.success(
                title='删除成功',
                content="项目 ["+self.text()+"] 删除成功👻",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=layout_parent
            )
            #项目根目录
            folder_path = cfg.get(cfg.projectFolder)
            # 项目目录
            project_path = folder_path + "/" + self.text()
            #删除项目目录及其子目录子文件
            try:
                import shutil
                shutil.rmtree(project_path)
                print("删除成功")
            except Exception as e:
                print("删除时发生错误:", e)


        except Exception as e:
            print("删除时发生错误:", e)

    #右键弹出菜单
    def contextMenuEvent(self, event):
        menu = RoundMenu(self)
        menu.addAction(Action(FluentIcon.DELETE,"删除"))
        menu.exec(event.globalPos())
        event.accept()
        #删除被单击执行方法
        menu.triggered.connect(lambda action:self.remove())

    #鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        #点击事件信息
        self.clicked.emit()
        #跳转页面
        try:
            #读取项目文件并转换为python字典
            # 项目根目录
            folder_path = cfg.get(cfg.projectFolder)
            # 项目目录
            project_path = folder_path + "/" + self.text()
            #读取目录下同名json文件
            with open(project_path + "/" + self.text() + ".json", "r", encoding="utf-8") as f:
                file = f.read()
                #转换为python字典
                file = eval(file)
                cfg.set(cfg.projectData, file)
            # 获取应用程序实例
            app = QApplication.instance()
            # 获取应用程序的主窗口
            main_window = app.activeWindow()
            main_window.mainInterface.initVisualizationList()
            main_window.switchTo(main_window.mainInterface)
        except Exception as e:
            print("跳转页面时发生错误:", e)




