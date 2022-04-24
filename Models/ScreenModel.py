from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QWidget, QStackedLayout, QLabel, QMainWindow, QTextEdit, QDockWidget
from PyQt5.uic import loadUi

from utils.createPDF import createPDF
from utils.dataManager import getDatas, updateData


class Screen(QWidget):

    def __init__(self, *args):
        super().__init__()

    def init_LineEdit(self, section: str, chapter: str = '', screen_number: str = ''):

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, (QLineEdit, QTextEdit)):
                    if chapter == '' and screen_number == '':
                        widget.setText(getDatas("user")[section][widget.objectName()])
                    elif chapter != '' and screen_number == '':
                        widget.setText(getDatas("user")[section][chapter])
                    else:
                        widget.setText(getDatas("user")[section][chapter][screen_number])
                    widget.textChanged.connect(lambda: self.input_changed(section, chapter, screen_number))
                    i = i + 1

    def input_changed(self, section: str, chapter: str = '', screen_number: str = ''):

        new_datas = getDatas('user')

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, (QLineEdit, QTextEdit)):

                    if chapter == '' and screen_number == '':
                        new_datas[section][widget.objectName()] = widget.text()
                    elif chapter != '' and screen_number == '':
                        new_datas[section][chapter] = widget.toPlainText()
                    else:
                        new_datas[section][chapter][screen_number] = widget.toPlainText()

                    updateData('user', new_datas)
                    i = i + 1

    def init_Label(self, title: str, question: str, image):

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, QLabel):
                    if widget.objectName() == "title":
                        widget.setText(title)
                    if widget.objectName() == "question":
                        widget.setText(question)
                    if widget.objectName == "image":
                        pixmap = QPixmap(image)
                        widget.setPixmap(pixmap)

    def navigation(self, goto: str):

        from navigator.Navigator import Navigators
        from navigator.MainNavigator import MainWindow

        for nav in Navigators:
            if nav.objectName() == goto:
                MainWindow.takeCentralWidget()
                MainWindow.setCentralWidget(nav)
                print(nav.objectName())
            for screen in nav.children():
                if not isinstance(screen, QStackedLayout):
                    print(screen.objectName())
                    if screen.objectName() == goto:
                        nav.setCurrentWidget(screen)


class MainScreen(QMainWindow):

    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\AppScreen.ui', self)
        from navigator.MainNavigator import MainNavigator
        self.setCentralWidget(MainNavigator)


class MainWindowScreen(QMainWindow, Screen):

    def __init__(self):
        super(MainWindowScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\MainScreen.ui', self)

        self.verticalMenu.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.verticalMenu.setTitleBarWidget(QWidget())

        self.btn_basics.clicked.connect(lambda: self.navigation("BASICNavigator"))
        self.btn_materials.clicked.connect(lambda: self.navigation("MATERIALNavigator"))
        self.btn_report.clicked.connect(lambda: self.navigation("REPORTNavigator"))


class StartingScreen(QMainWindow, Screen):

    def __init__(self):
        super(StartingScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\page_accueil_centrée.ui', self)
        self.init_LineEdit("PERSONAL")
        self.btn_next.clicked.connect(lambda: self.navigation('MainWindow'))


class StaticScreen(QMainWindow, Screen):

    def __init__(self, *args):
        super().__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\Basics\MainBasicsScreen.ui', self)


class ReportScreen(QMainWindow, Screen):

    def __init__(self, chapter: str, screen_number: int, image: str = ''):

        super().__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\Report\window_resum.ui', self)

        self.chapter = chapter
        self.screen_number = screen_number
        self.image = image

        self.btn_pdf.clicked.connect(createPDF)

        self.init_navigation()

        self.question = getDatas('permanent')['REPORT'][self.chapter]

        if not isinstance(self.question, str):
            self.init_Label(self.chapter, self.question[str(self.screen_number)], self.image)
            self.init_LineEdit("REPORT", self.chapter, str(self.screen_number))
        else:
            self.init_Label(self.chapter, self.question, self.image)
            self.init_LineEdit("REPORT", self.chapter)

    def init_navigation(self):

        permanent_report = getDatas('permanent')['REPORT']
        max_number = 0

        for title in permanent_report:
            if not isinstance(permanent_report[title], str):
                max_number = max_number + len(permanent_report[title].items())
            else:
                max_number = max_number + 1

        if self.screen_number > 1:
            self.btn_previous.clicked.connect(lambda: self.navigation('REPORT' + str(self.screen_number - 1)))
        else:
            self.btn_previous.hide()

        if self.screen_number < max_number:
            self.btn_next.clicked.connect(lambda: self.navigation('REPORT' + str(self.screen_number + 1)))
        else:
            self.btn_next.hide()
