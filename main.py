import sys
from PyQt5.QtWidgets import QApplication

from Models.ScreenModel import MainScreen

app = QApplication(sys.argv)
main_screen = MainScreen()
main_screen.showMaximized()
sys.exit(app.exec_())
