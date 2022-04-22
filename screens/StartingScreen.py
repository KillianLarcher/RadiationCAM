import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi

from Models.ScreenModel import Screen


class StartingScreen(QMainWindow, Screen):

    def __init__(self):
        super(StartingScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\page_accueil_centrée.ui', self)
        self.init_lineEdit("PERSONAL")
        self.btn_next.clicked.connect(lambda: self.navigation('MainWindow'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    starting_screen = StartingScreen()
    starting_screen.showMaximized()
    sys.exit(app.exec_())
