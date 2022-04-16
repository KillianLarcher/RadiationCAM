from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class MainInfraredCameraScreen(QDialog):

    def __init__(self):
        super(MainInfraredCameraScreen, self).__init__()
        uic.loadUi('screens/MainInfraredCameraScreen.ui', self)
        # self.btn-ok.clicked.connect
        # self.btn-cancel.clicked.connect
        # self.btn-ok.clicked.connect
        # self.btn-cancel.clicked.connect
