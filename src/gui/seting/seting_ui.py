from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from qfluentwidgets import TitleLabel, SettingCardGroup, PushSettingCard, FluentIcon, SimpleCardWidget, CaptionLabel, \
    PrimaryPushButton, LineEdit

from src.utils.Config import cfg


class Seting_Ui(object):

    def setupUi(self, setting):
        setting.setObjectName("setting")
        self.layout = QVBoxLayout(setting)

        self.setingLabel = TitleLabel("设置", setting)
        self.layout.addWidget(self.setingLabel)


        self.projectSetingGroup = SettingCardGroup(
            self.tr("设置项目地址"))
        self.layout.addWidget(self.projectSetingGroup)
        self.projectFolderCard = PushSettingCard(
            self.tr('选择文件夹'),
            FluentIcon.DOWNLOAD,
            self.tr("项目文件夹"),
            cfg.get(cfg.projectFolder),
            self.projectSetingGroup
        )

        self.projectSetingGroup.addSettingCard(self.projectFolderCard)


        self.serviceSetingGroup = SettingCardGroup(
            self.tr("设置服务地址")
        )

        #创建一个水平布局
        self.servicecar = SimpleCardWidget(self.serviceSetingGroup)
        self.servicecar.setLayout(QHBoxLayout())
        #左侧显示地址 中间显示输入框 右侧显示确定按钮 使用水平布局

        self.servicetitle = TitleLabel("地址")
        self.servicelinedit = LineEdit()
        self.servicelinedit.setText(cfg.get(cfg.serverHost))
        self.serviceclick = PrimaryPushButton("确定")
        self.servicecar.layout().addWidget(self.servicetitle)
        self.servicecar.layout().addWidget(self.servicelinedit)
        self.servicecar.layout().addWidget(self.serviceclick)
        # self.serviceSetingGroup.addSettingCard(self.servicecar)



        self.layout.addWidget(self.serviceSetingGroup)
        self.layout.addWidget(self.servicecar)

        #添加Vertical Spacer 将内容撑起
        self.layout.addStretch(1)












