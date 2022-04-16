from PyQt5.QtWidgets import QStackedWidget

from screens.Basics.MainBasicsScreen import MainBasicsScreen

BasicsNavigator = QStackedWidget()

MainBasics = MainBasicsScreen()

BasicsNavigator.addWidget(MainBasics)

BasicsNavigator.setCurrentWidget(MainBasics)

