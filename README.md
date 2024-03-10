# 基于 python 的RPA 自动化软件



## 项目结构

```
ProjectName/
│
├── README.md          # 项目说明文件
├── requirements.txt   # 项目依赖库列表
├── setup.py           # 包打包与安装配置脚本（如果你打算发布为pip包）
│
├── src/               # 主要源码目录
│   ├── __init__.py    # 初始化文件，让src成为一个Python包
│
│   ├── main.py         # 程序主入口文件
│
│   ├── gui/            # PyQt相关UI及逻辑 
│   │   ├── __init__.py
│   │   ├── main_window.py     # 主窗口模块
│   │   ├── widget_elements/   # 自定义拖拽控件
│   │   │   ├── __init__.py
│   │   │   ├── click_widget.py  # 封装pyautogui点击操作的控件
│   │   │   ├── fill_widget.py   # 封装pyautogui填写操作的控件
│   │   │   └── ...              # 其他控件
│   │   └── browser_widget.py   # 封装selenium浏览器操作的控件或模块
│
│   ├── automation/      # 自动化核心逻辑部分
│   │   ├── __init__.py
│   │   ├── actions/       # 基础动作模块
│   │   │   ├── __init__.py
│   │   │   ├── mouse.py     # 鼠标操作封装
│   │   │   ├── keyboard.py   # 键盘操作封装
│   │   │   └── web.py        # selenium相关操作封装
│   │   └── workflow.py     # 工作流编排逻辑
│
│   └── utils/             # 工具函数和辅助类
│       ├── __init__.py
│       ├── config.py       # 项目配置文件
│       └── ...
│
├── resources/          # 存放资源文件，如图标、样式表等
│   ├── icons/
│   ├── styles/
│   └── ...

```

https://raw.hellogithub.com/hosts

![image-20240310201729485](F:\RPA\README\image-20240310201729485.png)







