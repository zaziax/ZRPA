# -*- coding: utf-8 -*-

# 此代码由 PyQt5 UI 代码生成器生成。
# 请注意：任何手动修改都将被后续运行的 pyuic5 覆盖。
# 请谨慎编辑。

from PyQt5 import QtCore, QtGui, QtWidgets

from src.gui.icon.Icon import Icon


class Main_Ui(object):
    def setupUi(self, home):
        """
        初始化主用户界面布局。

        参数:
        - home: 主窗口对象，用于设置窗口属性和布局。
        """
        # 设置窗口名称和大小
        home.setObjectName("home")
        home.resize(932, 825)

        # 设置主栅格布局
        self.gridLayout_2 = QtWidgets.QGridLayout(home)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # 设置主页面布局
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        # #创建一个占位的空weidget 最小高度45px
        # self.emptyWidget = QtWidgets.QWidget(home)
        # self.emptyWidget.setMaximumHeight(15)
        # self.emptyWidget.setObjectName("emptyWidget")
        # self.mainLayout.addWidget(self.emptyWidget)
        # 初始化头部工具栏并添加到布局
        self.HeaderToolBar = CommandBar(home)
        self.HeaderToolBar.setObjectName("HeaderToolBar")
        self.mainLayout.addWidget(self.HeaderToolBar)

        # 初始化内容布局
        self.Layout_content = QtWidgets.QHBoxLayout()
        self.Layout_content.setObjectName("Layout_content")

        # 初始化动作菜单布局
        self.ActionMenuLayout = SimpleCardWidget(home)
        self.ActionMenuLayout.setObjectName("ActionMenuLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ActionMenuLayout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 初始化动作列表标签并添加到动作菜单布局
        self.ActionListLabel = SimpleCardWidget(self.ActionMenuLayout)
        self.ActionListLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.ActionListLabel.setObjectName("ActionListLabel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ActionListLabel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ActionListLableIcon = IconWidget(self.ActionListLabel)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/jigsaw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ActionListLableIcon.setIcon(icon)
        self.ActionListLableIcon.setObjectName("ActionListLableIcon")
        self.horizontalLayout.addWidget(self.ActionListLableIcon)
        self.ActionListLabelName = CaptionLabel(self.ActionListLabel)
        self.ActionListLabelName.setProperty("pixelFontSize", 20)
        self.ActionListLabelName.setObjectName("ActionListLabelName")
        self.horizontalLayout.addWidget(self.ActionListLabelName)
        self.verticalLayout_2.addWidget(self.ActionListLabel)

        # 初始化动作列表并添加到动作菜单布局
        self.ActionList = TreeWidget(self.ActionMenuLayout)
        self.ActionList.setObjectName("ActionList")
        self.ActionList.headerItem().setText(0, "动作列表")
        self.verticalLayout_2.addWidget(self.ActionList)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.Layout_content.addWidget(self.ActionMenuLayout)

        # 初始化脚本编辑布局并添加到内容布局
        self.ScriptEditLayout = SimpleCardWidget(home)
        self.ScriptEditLayout.setObjectName("ScriptEditLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ScriptEditLayout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ScriptEditTab = QtWidgets.QTabWidget(self.ScriptEditLayout)

        self.ScriptEditTab.setObjectName("ScriptEditTab")


        # 初始化可视化编辑标签页并添加到脚本编辑布局
        self.VisualizationTab = QtWidgets.QWidget()
        self.VisualizationTab.setObjectName("VisualizationTab")
        self.gridLayout = QtWidgets.QGridLayout(self.VisualizationTab)
        self.gridLayout.setObjectName("gridLayout")
        self.VisualizationList = ListWidget(self.VisualizationTab)
        self.VisualizationList.setObjectName("VisualizationList")
        self.gridLayout.addWidget(self.VisualizationList, 0, 0, 1, 1)
        self.ScriptEditTab.addTab(self.VisualizationTab, "")
        # 设置 VisualizationList 风格为 DARK


        # 初始化源代码编辑标签页并添加到脚本编辑布局
        self.SourceCodeTab = QtWidgets.QWidget()
        self.SourceCodeTab.setObjectName("SourceCodeTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.SourceCodeTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SourceCodeEdit = PlainTextEdit(self.SourceCodeTab)
        self.SourceCodeEdit.setObjectName("SourceCodeEdit")
        self.gridLayout_3.addWidget(self.SourceCodeEdit, 0, 0, 1, 1)
        self.ScriptEditTab.addTab(self.SourceCodeTab, "")
        self.verticalLayout.addWidget(self.ScriptEditTab)
        self.Layout_content.addWidget(self.ScriptEditLayout)

        ##设置整个 tabwidget 风格为 DARK
        self.ScriptEditTab.setStyleSheet("QTabBar::tab {height: 30px; width: 100px;}"
                                        "QTabBar::tab:selected {background-color: #2c2c2c;}"
                                        "QTabBar::tab:!selected {background-color: #3c3c3c;}")
        self.ScriptEditTab.setCurrentIndex(0)
        self.ScriptEditTab.tabBar().setStyleSheet("QTabBar::tab {height: 30px; width: 100px;}"
                                        "QTabBar::tab:selected {background-color: #2c2c2c;}"
                                        "QTabBar::tab:!selected {background-color: #3c3c3c;}")



        # #设置tabwidget 的widget部分风格为 DARK
        # self.ScriptEditTab.setStyleSheet("QTabWidget::pane {border: 1px solid #2c2c2c;}"
        #                                 "QTabWidget::tab-bar {alignment: center;}"
        #                                 "QTabBar::tab {height: 30px; width: 100px;}"
        #                                 "QTabBar::tab:selected {background-color: #2c2c2c;}"
        #                                 "QTabBar::tab:!selected {background-color:#3c3c3c;}")
        # self.ScriptEditTab.tabBar().setStyleSheet("QTabWidget::pane {border: 1px solid #2c2c2c;}"
        #                                 "QTabWidget::tab-bar {alignment: center;}"
        #                                 "QTabBar::tab {height: 30px; width: 100px;}"
        #                                 "QTabBar::tab:selected {background-color: #2c2c2c;}"
        #                                 "QTabBar::tab:!selected {background-color:#3c3c3c;}")

        self.ScriptEditTab.tabBar().setTabTextColor(0, QColor(255, 255, 255))
        self.ScriptEditTab.tabBar().setTabTextColor(1, QColor(255, 255, 255))
        self.ScriptEditTab.tabBar().setTabText(0, "可视化编辑")
        self.ScriptEditTab.tabBar().setTabText(1, "源代码编辑")
        self.ScriptEditTab.tabBar().setTabIcon(0,Icon('mouse').icon)
        self.ScriptEditTab.tabBar().setTabIcon(1,Icon('mouse').icon)
        self.ScriptEditTab.tabBar().setTabToolTip(0, "可视化编辑")
        self.ScriptEditTab.tabBar().setTabToolTip(1, "源代码编辑")
        self.ScriptEditTab.tabBar().setTabEnabled(0, True)
        self.ScriptEditTab.tabBar().setTabEnabled(1, True)
        self.ScriptEditTab.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide, None)
        self.ScriptEditTab.tabBar().setTabButton(1, QtWidgets.QTabBar.RightSide, None)

        # 设置ScriptEditTab的widget 为 qfluentwidgets 的 SimpleCardWidget
        self.ScriptEditTab.setStyleSheet("QTabWidget::pane {border: 1px solid #2c2c2c;}"
                                        "QTabWidget::tab-bar {alignment: center;}"
                                        "QTabBar::tab {height: 30px; width: 100px;}"
                                        "QTabBar::tab:selected {background-color: #2c2c2c;}"
                                        "QTabBar::tab:!selected {background-color:#3c3c3c;}")
        self.ScriptEditTab.tabBar().setStyleSheet("QTabWidget::pane {border: 1px solid #2c2c2c;}"
                                        "QTabWidget::tab-bar {alignment: center;}"
                                        "QTabBar::tab {height: 30px; width: 100px;}"
                                        "QTabBar::tab:selected {background-color: #2c2c2c;}"
                                        "QTabBar::tab:!selected {background-color:#3c3c3c;}")
        self.ScriptEditTab.tabBar().setTabTextColor(0, QColor(255, 255, 255))
        self.ScriptEditTab.tabBar().setTabTextColor(1, QColor(255, 255, 255))




        # 初始化属性布局并添加到内容布局
        self.AttributeLayout = SimpleCardWidget(home)
        self.AttributeLayout.setObjectName("AttributeLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AttributeLayout)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AttributeList = ListWidget(self.AttributeLayout)
        self.AttributeList.setObjectName("AttributeList")
        self.verticalLayout_3.addWidget(self.AttributeList)
        self.Layout_content.addWidget(self.AttributeLayout)

        # 设置内容布局的伸缩属性
        self.Layout_content.setStretch(0, 3)
        self.Layout_content.setStretch(1, 9)
        self.Layout_content.setStretch(2, 2)

        # 将内容布局添加到主页面布局
        self.mainLayout.addLayout(self.Layout_content)
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 15)

        # 将主页面布局添加到主栅格布局
        self.gridLayout_2.addLayout(self.mainLayout, 0, 0, 1, 1)

        # 翻译界面文字
        self.retranslateUi(home)
        self.ScriptEditTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        """
        翻译用户界面文本。
        """
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Form"))
        self.ActionListLabelName.setText(_translate("home", "动作列表"))
        self.ScriptEditTab.setTabText(self.ScriptEditTab.indexOf(self.VisualizationTab), _translate("home", "可视化"))
        self.ScriptEditTab.setTabText(self.ScriptEditTab.indexOf(self.SourceCodeTab), _translate("home", "序列化"))
from qfluentwidgets import CaptionLabel, CommandBar, IconWidget, ListWidget, PlainTextEdit, SimpleCardWidget, \
    TreeWidget, QColor
from src.resources.img import  rpa_rc
