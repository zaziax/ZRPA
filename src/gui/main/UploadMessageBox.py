from qfluentwidgets import SubtitleLabel, LineEdit, MessageBoxBase, PasswordLineEdit


class UploadMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('输入用户名密码')

        self.usernameLineEdit = LineEdit()
        self.usernameLineEdit.setPlaceholderText('输入用户名')
        self.usernameLineEdit.setClearButtonEnabled(True)

        self.passwordLineEdit = PasswordLineEdit()
        self.passwordLineEdit.setPlaceholderText('输入密码')
        self.passwordLineEdit.setClearButtonEnabled(True)

        #备注
        self.noteLineEdit = LineEdit()
        self.noteLineEdit.setPlaceholderText('输入备注')
        self.noteLineEdit.setClearButtonEnabled(True)

        # 将组件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.usernameLineEdit)
        self.viewLayout.addWidget(self.passwordLineEdit)
        self.viewLayout.addWidget(self.noteLineEdit)

        # 设置对话框的最小宽度
        self.widget.setMinimumWidth(350)


