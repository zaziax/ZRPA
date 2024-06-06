from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QFileDialog
from qfluentwidgets import InfoBar, InfoBarPosition

from src.gui.seting import Seting_Ui
from src.utils.Config import cfg


class SettingInterface(QWidget,Seting_Ui):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.projectFolderCard.clicked.connect(self.onProjectFolderCardClicked)
        self.serviceclick.clicked.connect(self.onServicerClicked)

    def onProjectFolderCardClicked(self):
        folder = QFileDialog.getExistingDirectory(
            self, self.tr("选中文件夹"), "./")
        if not folder or cfg.get(cfg.projectFolder) == folder:
            return

        cfg.set(cfg.projectFolder, folder)
        self.projectFolderCard.setContent(folder)
        # 提示更新成功
        InfoBar.success(
            title='更新成功',
            content="项目地址更新成功!✅",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def onServicerClicked(self):
        try:
            host = self.servicelinedit.text()
            cfg.set(cfg.serverHost, host)
            #提示更新成功
            InfoBar.success(
                title='更新成功',
                content="服务端地址更新成功！⚙️",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )
        except Exception as e:
            print(e)
