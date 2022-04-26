from PyQt5.QtWidgets import QStackedWidget

from Models.ScreenModel import DynamicScreen, StaticScreen, StartingScreen, MainWindowScreen
from utils.dataManager import getDatas

screens = {}

for key, value in getDatas('permanent').items():
    if key == 'REPORT':
        screens[key] = DynamicScreen
    else:
        screens[key] = StaticScreen

MainNavigator = QStackedWidget()

Starting = StartingScreen("PERSONAL")
MainWindow = MainWindowScreen()

MainNavigator.addWidget(Starting)
MainNavigator.addWidget(MainWindow)

MainNavigator.setCurrentWidget(Starting)

Navigators = [MainNavigator]

for section, screen in screens.items():

    Navigator = QStackedWidget()
    Navigator.setObjectName(section + "Navigator")

    datas = getDatas('permanent')[section]

    i = 1
    for title in datas:
        if not isinstance(datas[title], str):
            for key, value in datas[title].items():
                MyScreen = screen(section, title, i, "Image1.png")
                MyScreen.setObjectName(section + str(i))
                Navigator.addWidget(MyScreen)
                i = i + 1
        else:
            MyScreen = screen(section, title, i, "Image1.png")
            MyScreen.setObjectName(section + str(i))
            Navigator.addWidget(MyScreen)
            i = i + 1

    Navigators.append(Navigator)
