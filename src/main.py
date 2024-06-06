import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from src.gui.main_window import MainWindow
import ctypes

if __name__ == '__main__':

   ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

   QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
   QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
   QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())


