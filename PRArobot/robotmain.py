import os
import sys
import platform
import zipfile
import io

from PyQt5.QtCore import Qt, QUrl, QTimer
import socket
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QWidget, QMessageBox
from pip._vendor import requests
from qfluentwidgets import RoundMenu, setTheme, Theme, InfoBar, InfoBarPosition, json
from methods import *
import socketio
from PRArobot.RobotConfig import rfg
from robotmain_ui import Ui_Robot
from src.gui.icon import Icon


class MainWindow(QMainWindow,Ui_Robot):
    def __init__(self):
        super().__init__()
        self.websocket = None
        setTheme(Theme.DARK)
        self.setupUi(self)
        self.initUI()

        # 异步连接 WebSocket
        self.sio = socketio.Client()
        self.sio.on('connect', self.on_connect)
        self.sio.on('server_response', self.handle_server_response)
        self.sio.on('disconnect', self.on_disconnect)
        self.sio.on('taskstatus', self.taskstatus)
        self.sio.connect('http://localhost:5000')

        self.set_automation_method()

    def initUI(self):
        # 设置窗口标题和图标
        setTheme(Theme.DARK)
        self.setWindowTitle("配置执行器")
        #设置初始值
        self.serverhost.setText(rfg.get(rfg.serverHost))
        self.projectdir.setText(rfg.get(rfg.projectFolder))
        self.StrongBodyLabel.setText(rfg.get(rfg.robotuuid))


        self.setserverhost.setIcon(Icon('set').icon)
        self.setserverhost.clicked.connect(self.set_server_host)
        self.setprojectdir.setIcon(Icon('set').icon)
        self.setprojectdir.clicked.connect(self.set_project_dir)

        self.initbutton.clicked.connect(self.init_robot)


        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(Icon('roboticon').icon, self)
        self.setWindowIcon(QIcon(':/icon/roboticon.png'))

        # 创建托盘菜单和动作
        self.tray_menu = RoundMenu(self)
        self.show_action = QAction("设置", self)
        self.exit_action = QAction("退出", self)
        self.show_action.triggered.connect(self.showMainWindow)
        self.exit_action.triggered.connect(self.exitApplication)
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.exit_action)
        # 将托盘菜单设置给系统托盘图标
        self.tray_icon.setContextMenu(self.tray_menu)
        # 显示系统托盘图标
        self.tray_icon.show()



    def showMainWindow(self):
        # 显示主窗口
        self.showNormal()

    def exitApplication(self):
        # 退出应用程序
        self.tray_icon.hide()
        QApplication.quit()

    def set_server_host(self):
        rfg.set(rfg.serverHost, self.serverhost.text())
        InfoBar.success(
            title='更新成功',
            content="服务端地址更新成功!✅",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def set_project_dir(self):
        rfg.set(rfg.projectFolder, self.projectdir.text())
        InfoBar.success(
            title='更新成功',
            content="项目地址更新成功!✅",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self
        )

    def init_robot(self):
        #注册终端
        # 向flask服务器发起请求
        try:
            #获取服务端地址
            server_host = rfg.get(rfg.serverHost)
            # 弹出widget 输入用户名密码

            username = self.username.text()
            password = self.PasswordLineEdit.text()

            hostname = socket.gethostname()
            systemname = platform.system()


            response = requests.post(
                server_host + '/terminalinit/',
                data={'username': username, 'password': password,'hostname':hostname,'systemname': systemname}
            )
            print(response.status_code)
            #发起请求
            if response.status_code == 200:
                InfoBar.success(
                    title='初始化成功',
                    content="初始化终端设备成功",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self
                )
                uuid = response.json()['msg']
                rfg.set(rfg.robotuuid, uuid)
            else:
                InfoBar.warning(
                    title='初始化失败',
                    content="初始终端设备失败！",
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM,
                    duration=-1,  # 永不消失
                    parent=self
                )
        except Exception as e:
            print(e)


    def on_connect(self):
        # 连接成功后发送 UUID
        self.sio.emit('setstatus', {'robotuuid': rfg.get(rfg.robotuuid)})
        # self.sio.emit('setstatus', {'robotuuid': 'your-uuid-here'})
        print('Connected to server')

    def handle_server_response(self, data):
        #在接收到 server_response 事件时被调用
        print('Received response from server:', data)

    def on_disconnect(self):
        print('Disconnected from server')

    def taskstatus(self, data):
        print('响应数据:', data)
        # 从字典中获取终端id
        uuidlist = data['terminal_id']
        print('设备列表:',uuidlist)
        print('终端id:',rfg.get(rfg.robotuuid))
        # 遍历终端id列表看是否有自己
        if rfg.get(rfg.robotuuid) in uuidlist:
            # 获取任务状态
            task_id = data['task_id']
            # 获取任务名称
            task_name = data['task_name']
            #脚本id
            script_id = data['script_id']
            # 获取脚本名称
            script_name = data['script_name']
            #查看本地是否有该项目文件夹
            if os.path.exists(rfg.get(rfg.projectFolder) + '/' + script_name):
                #有则运行脚本
                self.run(task_id,task_name,script_id,script_name)
            else:
                #向服务端发起请求下载脚本的压缩包
                #将压缩包解压到项目目录 删除压缩包
                response = requests.post(
                    rfg.get(rfg.serverHost) + '/download/',
                    data={'script_id':script_id,'uuid': rfg.get(rfg.robotuuid)}
                    )
                if response.status_code == 200:
                    # 获取压缩包内容
                    compressed_data = response.content
                    # 解压压缩包到项目目录
                    with zipfile.ZipFile(io.BytesIO(compressed_data)) as zip_file:
                        zip_file.extractall(rfg.get(rfg.projectFolder)+'/'+script_name)
                    self.run(task_id, task_name, script_id, script_name)




  #运行流程的方法
    def run(self,task_id,task_name,script_id,script_name):
        try:
            # 获取项目根目录
            folder_path = rfg.get(rfg.projectFolder)
            # 获取项目名
            project_name = script_name
            # 获取项目目录
            project_path = folder_path + '/' + project_name
            # 获取项目json文件
            json_file = project_path + '/' + project_name + '.json'
            # 获取项目json文件内容
            with open(json_file, 'r',encoding='utf-8') as f:
                data = json.load(f)
            actions = data['actions']
            print("actions:",actions)
            #延时
            time.sleep(2)
            #遍历执行方法 method 的 value 对应执行的方法 properties是填入方法的参数
            for action in actions:
                method = action['method']
                properties = action['properties']
                print("method:",method)
                print("properties:",properties)
                #执行方法
                automethod = self.AUTOMATION_METHOD.get(method)
                automethod(**properties)
            self.sio.emit('taskresults', {'task_id': task_id,
                                          'task_name': task_name,
                                          'status':'已结束',
                                          'result':'机器'+rfg.get(rfg.robotuuid)+'成功执行任务'+task_name })


        except Exception as e:
            self.sio.emit('taskresults', {'task_id': task_id,
                                          'task_name': task_name,
                                          'status': '异常',
                                          'result': '机器' + rfg.get(rfg.robotuuid) + '执行流程过程中出现错误，错误详情:'+str(e)})
            print(e)


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


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(400, 350)
    sys.exit(app.exec_())