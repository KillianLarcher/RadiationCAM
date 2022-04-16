from os.path import abspath

from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.uic import loadUi
import os.path


class TestReportScreen(QDialog):

    def __init__(self):
        super(TestReportScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\MainScreen.ui', self)
        self.buttonBox.clicked.connect(self.NextPage)

    def NextPage(self):
        from navigator.ReportNavigator import ReportNavigator, TestReport
        ReportNavigator.removeWidget(self)
        ReportNavigator.setCurrentIndex(self, 0)
