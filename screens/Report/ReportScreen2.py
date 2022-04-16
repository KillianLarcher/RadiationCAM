from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.uic import loadUi


class ReportScreen2(QWidget):

    def __init__(self):
        super(ReportScreen2, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\next.ui', self)
        self.pushButton.clicked.connect(self.previous_page)

    def previous_page(self):
        from navigator.ReportNavigator import ReportNavigator, Report1
        ReportNavigator.setCurrentWidget(Report1)

