from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QLineEdit, QWidget, QStackedLayout, QLabel, QMainWindow, QTextEdit, QDockWidget
from PyQt5.uic import loadUi

from utils.createPDF import createPDF
from utils.dataManager import getDatas, updateData


class Screen(QWidget):

    def __init__(self, section: str = '', chapter: str = '', screen_number: int = 0, picture: str = ''):

        super().__init__()
        self.section = section
        self.chapter = chapter
        self.screen_number = screen_number
        self.picture = picture
        self.player = QMediaPlayer()

        try:
            self.question_text = getDatas('permanent')[self.section][self.chapter]
        except KeyError:
            self.question_text = None

    def init_LineEdit(self):

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, (QLineEdit, QTextEdit)):

                    if self.chapter == '' and self.screen_number == 0:
                        widget.setText(getDatas("user")[self.section][widget.objectName()])
                    else:
                        try:
                            widget.setText(getDatas("user")[self.section][self.chapter])
                        except:
                            widget.setText(getDatas("user")[self.section][self.chapter][str(self.screen_number)])

                    widget.textChanged.connect(lambda: self.input_changed())
                    i = i + 1

    def input_changed(self):

        new_datas = getDatas('user')

        for layouts in self.children():
            i = 0
            for widget in layouts.children():
                if isinstance(widget, (QLineEdit, QTextEdit)):

                    if self.chapter == '' and self.screen_number == 0:
                        new_datas[self.section][widget.objectName()] = widget.text()
                    elif self.chapter != '' and self.screen_number == 0:
                        new_datas[self.section][self.chapter] = widget.toPlainText()
                    else:
                        new_datas[self.section][self.chapter][self.screen_number] = widget.toPlainText()

                    updateData('user', new_datas)
                    i = i + 1

    def init_Label(self):

        if isinstance(self.question_text, dict):
            self.setLabel("title", self.chapter)
            self.setLabel("question", self.question_text[str(self.screen_number)])
            self.setLabel("image", self.picture)

        if isinstance(self.question_text, str):
            self.setLabel("title", self.chapter)
            self.setLabel("question", self.question_text)
            self.setLabel("image", self.picture)

    def setLabel(self, title: str = '', content: str = ''):

        path = ''

        for layouts in self.children():
            if isinstance(layouts, QLabel):
                if layouts.objectName() == title:
                    if content.find('.png') != -1:
                        pixmap = QPixmap(path + '/img/' + content)
                        layouts.setPixmap(pixmap)
                    elif content.find('.avi') != -1:
                        pass
                else:
                    layouts.setText(content)

            for widget in layouts.children():
                if isinstance(widget, QLabel):
                    if widget.objectName() == title:
                        if content.find('.png') != -1:
                            pixmap = QPixmap(path + './img/' + content)
                            widget.setPixmap(pixmap)
                        elif content.find('.avi') != -1:
                            widget2 = QVideoWidget(widget)
                            widget2.resize(500, 500)
                            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(
                                './video/test.avi')))
                            self.btn_play.show()
                            self.btn_play.clicked.connect(lambda: self.play_video(widget2))
                            pass
                        else:
                            widget.setText(content)

    def play_video(self, widget):
        self.player.setVideoOutput(widget)
        self.player.play()

    @staticmethod
    def navigation(goto: str):

        from navigator.Navigator import Navigators
        from navigator.Navigator import MainWindow

        for nav in Navigators:
            if nav.objectName() == goto:
                MainWindow.takeCentralWidget()
                MainWindow.setCentralWidget(nav)
            for screen in nav.children():
                if not isinstance(screen, QStackedLayout):
                    if screen.objectName() == goto:
                        nav.setCurrentWidget(screen)

    def init_navigation(self):

        permanent_report = getDatas('permanent')[self.section]
        max_number = 0

        for title in permanent_report:
            if not isinstance(permanent_report[title], str):
                max_number = max_number + len(permanent_report[title].items())
            else:
                max_number = max_number + 1

        if self.screen_number > 1:
            self.btn_previous.clicked.connect(lambda: self.navigation(self.section + str(self.screen_number - 1)))
        else:
            self.btn_previous.hide()

        if self.screen_number < max_number:
            self.btn_next.clicked.connect(lambda: self.navigation(self.section + str(self.screen_number + 1)))
        else:
            self.btn_next.hide()


class MainScreen(QMainWindow, Screen):

    def __init__(self):
        super().__init__()
        loadUi('./.ui/AppScreen.ui', self)
        from navigator.Navigator import MainNavigator
        self.setCentralWidget(MainNavigator)


class StartingScreen(QMainWindow, Screen):

    def __init__(self, section: str):
        super(StartingScreen, self).__init__(section)

        loadUi('./.ui/StartingScreen.ui', self)
        self.init_LineEdit()
        self.btn_next.clicked.connect(lambda: self.navigation('MainWindow'))


class MainWindowScreen(QMainWindow, Screen):

    def __init__(self):
        super(MainWindowScreen, self).__init__()
        loadUi('./.ui/MainScreen.ui', self)

        self.verticalMenu.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.verticalMenu.setTitleBarWidget(QWidget())

        self.btn_basics.clicked.connect(lambda: self.navigation("BASICNavigator"))
        self.btn_materials.clicked.connect(lambda: self.navigation("MATERIALNavigator"))
        self.btn_report.clicked.connect(lambda: self.navigation("REPORTNavigator"))


class StaticScreen(QMainWindow, Screen):

    def __init__(self, section: str, chapter: str = '', screen_number: int = 0, picture: str = ''):
        super().__init__(section, chapter, screen_number, picture)

        loadUi('./.ui/StaticScreen.ui', self)

        self.init_navigation()
        self.init_Label()


class DynamicScreen(QMainWindow, Screen):

    def __init__(self, section: str, chapter: str, screen_number: int = 0, picture: str = ''):
        super().__init__(section, chapter, screen_number, picture)

        loadUi('./.ui/DynamicScreen.ui', self)

        self.btn_pdf.clicked.connect(createPDF)

        self.btn_play.hide()

        self.init_navigation()
        self.init_LineEdit()
        self.init_Label()
