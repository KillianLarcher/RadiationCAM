from PyQt5.QtWidgets import QStackedWidget

from screens.Report.MainReportScreen import MainReportScreen
from screens.Report.ReportScreen1 import ReportScreen1
from screens.Report.ReportScreen2 import ReportScreen2

ReportNavigator = QStackedWidget()

MainReport = MainReportScreen()
Report1 = ReportScreen1()
Report2 = ReportScreen2()

ReportNavigator.addWidget(MainReport)
ReportNavigator.addWidget(Report1)
ReportNavigator.addWidget(Report2)

ReportNavigator.setCurrentWidget(MainReport)

