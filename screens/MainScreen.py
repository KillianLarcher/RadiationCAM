import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi


class MainScreen(QMainWindow):

    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\themain.ui', self)
        from navigator.MainNavigator import MainNavigator
        self.setCentralWidget(MainNavigator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_screen = MainScreen()
    main_screen.showMaximized()
    sys.exit(app.exec_())
