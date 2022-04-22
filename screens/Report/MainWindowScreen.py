import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget
from PyQt5.uic import loadUi
from screens.StartingScreen import StartingScreen


# TODO signal ?


class MainWindowScreen(QMainWindow):

    def __init__(self):
        super(MainWindowScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\MainScreen.ui', self)

        self.verticalMenu.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.verticalMenu.setTitleBarWidget(QWidget())

        self.btn_basics.clicked.connect(self.goto_BasicsNavigator)
        self.btn_materials.clicked.connect(self.goto_MaterialsNavigator)
        self.btn_report.clicked.connect(self.goto_ReportNavigator)


    def goto_BasicsNavigator(self):
        self.takeCentralWidget()
        from navigator.BasicsNavigator import BasicsNavigator
        self.setCentralWidget(BasicsNavigator)

    def goto_MaterialsNavigator(self):
        self.takeCentralWidget()
        from navigator.MaterialsNavigator import MaterialsNavigator
        self.setCentralWidget(MaterialsNavigator)

    def goto_ReportNavigator(self):
        self.takeCentralWidget()
        from navigator.ReportNavigator import ReportNavigator
        self.setCentralWidget(ReportNavigator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MainWindowScreen()
    test.showMaximized()
    sys.exit(app.exec_())
