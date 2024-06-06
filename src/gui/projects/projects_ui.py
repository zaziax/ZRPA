
from PyQt5.QtCore import QEasingCurve
from qfluentwidgets import FlowLayout, PushButton
from src.gui.projects import MessageBox,ProjectItem

class Projects_Ui(object):
    def setupUi(self, project):
        """
        设置项目布局。
        """
        # 设置项目对象的名称
        project.setObjectName("project")

        # 创建带有动画效果的FlowLayout布局
        self.layout = FlowLayout(project,needAni=True)
        # 设置自定义动画参数
        self.layout.setAnimation(250, QEasingCurve.OutQuad)

        # 设置布局的外边距和间距
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setVerticalSpacing(20)
        self.layout.setHorizontalSpacing(10)

        # 创建并设置项目项，显示"+"号
        self.item = ProjectItem()
        self.item.set_item_text("+")

        # 将项目项添加到布局中
        self.layout.addWidget(self.item)

        # 调整窗口大小
        self.resize(250, 300)








