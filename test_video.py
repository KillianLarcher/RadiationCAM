from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import sys

app = QApplication(sys.argv)
w = QVideoWidget()
w.resize(300, 300)
w.move(0, 0)
w.show()
player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\video\test.avi')))
player.setVideoOutput(w)
player.play()
sys.exit(app.exec_())
