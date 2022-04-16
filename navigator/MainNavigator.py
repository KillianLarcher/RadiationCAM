import sys
from PyQt5.QtWidgets import QStackedWidget, QApplication

from screens.StartingScreen import StartingScreen
from screens.Report.MainWindowScreen import MainWindowScreen

MainNavigator = QStackedWidget()

Starting = StartingScreen()
MainWindow = MainWindowScreen()

MainNavigator.addWidget(Starting)
MainNavigator.addWidget(MainWindow)

MainNavigator.setCurrentWidget(Starting)

