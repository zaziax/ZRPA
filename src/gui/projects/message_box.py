from qfluentwidgets import SubtitleLabel, LineEdit, MessageBoxBase


class MessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('新建项目')
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('输入项目名称')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)


