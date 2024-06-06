
from qfluentwidgets import (qconfig, QConfig, ConfigItem, FolderValidator)



class RobotConfig(QConfig):
    """ Config of application """

    projectFolder = ConfigItem(
        "Folders", "project", "app/robotproject", FolderValidator())

    projectData = ConfigItem(
        "Data", "project", {},
    )

    serverHost = ConfigItem(
        "Server", "host", "http://127.0.0.1:5000",
    )

    robotuuid = ConfigItem(
        "Data", "robotuuid", "",
    )


rfg = RobotConfig()
qconfig.load('app/robotconfig/robotconfig.json', rfg)

# PROJECT = {}