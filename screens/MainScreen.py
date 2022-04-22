import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainScreen(QMainWindow):

    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\AppScreen.ui', self)
        from navigator.MainNavigator import MainNavigator
        self.setCentralWidget(MainNavigator)


app = QApplication(sys.argv)
main_screen = MainScreen()
main_screen.showMaximized()
sys.exit(app.exec_())
