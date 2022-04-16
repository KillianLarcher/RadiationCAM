import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from dataManager import updateData


class StartingScreen(QWidget):

    def __init__(self):
        super(StartingScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\StartingScreen.ui', self)
        self.input_name.textChanged.connect(self.input_changed)
        self.btn_start.clicked.connect(self.starting)

    def input_changed(self):
        updateData("name", self.input_name.text())

    def starting(self):
        from navigator.MainNavigator import MainNavigator, MainWindow
        MainNavigator.setCurrentWidget(MainWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    starting_screen = StartingScreen()
    starting_screen.showMaximized()
    sys.exit(app.exec_())
