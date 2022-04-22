import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from Models.ScreenModel import Screen, ReportScreen


class MainReportScreen(QMainWindow, ReportScreen):

    def __init__(self):
        super().__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\Report\window_resum.ui', self)

        self.init_lineEdit("REPORT")
        self.btn_next.clicked.connect(lambda: self.navigation('Report2'))


if __name__ == "__main__":
    app = QApplication([])
    window = MainReportScreen()
    window.show()
    sys.exit(app.exec_())
