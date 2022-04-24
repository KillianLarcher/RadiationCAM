from PyQt5.QtWidgets import QStackedWidget

from Models.ScreenModel import MainWindowScreen, StartingScreen

MainNavigator = QStackedWidget()

Starting = StartingScreen()
MainWindow = MainWindowScreen()

MainNavigator.addWidget(Starting)
MainNavigator.addWidget(MainWindow)

MainNavigator.setCurrentWidget(Starting)

