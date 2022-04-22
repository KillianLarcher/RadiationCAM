from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from PyQt5.uic import loadUi
import sys

from utils.dataManager import updateData, getDatas


class ReportScreen1(QWidget):

    def __init__(self):
        super(ReportScreen1, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\Report\previous.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    report_screen1 = ReportScreen1()
    report_screen1.showMaximized()
    sys.exit(app.exec_())
