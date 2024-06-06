from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from qfluentwidgets import SplitFluentWindow, setThemeColor
from qfluentwidgets import setTheme, Theme
from qfluentwidgets import FluentIcon as FIF, MSFluentWindow, NavigationItemPosition, NavigationAvatarWidget

from src.gui.main.main_interface import MainInterface
from src.gui.projects.projects_interface import ProjectsInterface
from src.gui.seting.seting_interface import SettingInterface
from src.utils.Config import cfg

class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        cfg.set(cfg.projectData,{})
        setTheme(Theme.DARK)
        self.setWindowTitle("Z-RPA")
        self.setWindowIcon(QIcon(':/icon/zrpaicon.png'))
        # setThemeColor("#cccccc")
        #为主页面设置默认大小保存居中
        # self.move(300, 100)
        self.resize(1300, 700)
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)


        #添加子页面
        self.projectsInterface = ProjectsInterface(self)
        self.addSubInterface(self.projectsInterface,FIF.BOOK_SHELF,'项目管理')

        self.mainInterface = MainInterface(self)
        self.addSubInterface(self.mainInterface,FIF.ROBOT,'流程编辑')

        #添加作者页面
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('zazia',':/icon/avatar.jpg'),
            position=NavigationItemPosition.BOTTOM
        )
        try:
            self.settingInterface = SettingInterface(self)
            #添加设置页面

            self.addSubInterface(
                self.settingInterface,
                FIF.SETTING,
                self.tr('设置'),
                position=NavigationItemPosition.BOTTOM
                )

        except Exception as e:
            print(e)



