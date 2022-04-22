from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QLineEdit, QWidget, QStackedLayout
from utils.dataManager import getDatas, updateData


class Screen(QWidget):
    def __init__(self):
        super().__init__()

    def init_lineEdit(self, category: str):

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, QLineEdit):
                    widget.setText(getDatas("user")[category][widget.objectName()])
                    widget.textChanged.connect(lambda: self.input_changed(category))
                    i = i + 1

    def input_changed(self, category: str):

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, QLineEdit):
                    print(widget.objectName())
                    new_datas = getDatas('user')[category]
                    new_datas[widget.objectName()] = widget.text()
                    updateData('user', category, new_datas)
                    print('ok')
                    i = i + 1

    def navigation(self, goto_screen: str):

        from navigator.MainNavigator import MainNavigator
        from navigator.ReportNavigator import ReportNavigator
        from navigator.MaterialsNavigator import MaterialsNavigator
        from navigator.BasicsNavigator import BasicsNavigator

        navigators = [MainNavigator, ReportNavigator, MaterialsNavigator, BasicsNavigator]

        for nav in navigators:
            for QObject in nav.children():
                if not isinstance(QObject, QStackedLayout):
                    print("name : ", QObject.objectName())
                    if QObject.objectName() == goto_screen:
                        print('ok')
                        navigator = nav
                        screen = QObject
                        navigator.setCurrentWidget(screen)


class ReportScreen(Screen):
    def __init__(self):
        super().__init__()
        self.init_lineEdit("REPORT")
