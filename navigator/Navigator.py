from PyQt5.QtWidgets import QStackedWidget

from Models.ScreenModel import ReportScreen, StaticScreen
from navigator.MainNavigator import MainNavigator
from utils.dataManager import getDatas

screens = {}

for key, value in getDatas('permanent').items():
    if key == 'REPORT':
        screens[key] = ReportScreen
    else:
        screens[key] = StaticScreen

Navigators = [MainNavigator]

for section, screen in screens.items():

    Navigator = QStackedWidget()
    Navigator.setObjectName(section + "Navigator")

    datas = getDatas('permanent')[section]

    i = 1
    for title in datas:
        if not isinstance(datas[title], str):
            for key, value in datas[title].items():
                MyScreen = screen(title, i, "image.jpeg")
                MyScreen.setObjectName(section + str(i))
                Navigator.addWidget(MyScreen)
                i = i + 1
        else:
            MyScreen = screen(title, i, "image.jpeg")
            MyScreen.setObjectName(section + str(i))
            Navigator.addWidget(MyScreen)
            i = i + 1

    Navigators.append(Navigator)
