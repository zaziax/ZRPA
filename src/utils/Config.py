
from qfluentwidgets import (qconfig, QConfig, ConfigItem, FolderValidator)



class Config(QConfig):
    """ Config of application """

    projectFolder = ConfigItem(
        "Folders", "project", "app/project", FolderValidator())

    projectData = ConfigItem(
        "Data", "project", {},
    )

    serverHost = ConfigItem(
        "Server", "host", "http://127.0.0.1:5000",
    )


cfg = Config()
qconfig.load('app/config/config.json', cfg)

# PROJECT = {}