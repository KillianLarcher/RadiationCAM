from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


class MainMaterialsScreen(QWidget):

    def __init__(self):
        super(MainMaterialsScreen, self).__init__()
        loadUi(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\.ui\Materials\MainMaterialsScreen.ui', self)
        # self.btn-ok.clicked.connect
        # self.btn-cancel.clicked.connect
        # self.btn-ok.clicked.connect
        # self.btn-cancel.clicked.connect
