from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from PyQt5.uic import loadUi
import sys


class ReportScreen1(QWidget):

    def __init__(self):
        super(ReportScreen1, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\previous.ui', self)
        self.pushButton.clicked.connect(self.next_page)

    def next_page(self):
        from navigator.ReportNavigator import ReportNavigator, Report2
        ReportNavigator.setCurrentWidget(Report2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    report_screen1 = ReportScreen1()
    report_screen1.showMaximized()
    sys.exit(app.exec_())
