import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi


class MainReportScreen(QWidget):

    def __init__(self):
        super(MainReportScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\main.ui', self)
        self.btn_previous.clicked.connect(self.previous_page)
        self.btn_next.clicked.connect(self.next_page)
        self.setFixedWidth(800)
        self.setFixedHeight(800)

    def previous_page(self):
        from navigator.ReportNavigator import ReportNavigator, Report1
        ReportNavigator.setCurrentWidget(Report1)

    def next_page(self):
        from navigator.ReportNavigator import ReportNavigator, Report2
        ReportNavigator.setCurrentWidget(Report2)


if __name__ == "__main__":

    app = QApplication([])
    window = MainReportScreen()
    window.show()
    sys.exit(app.exec_())
