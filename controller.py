from PyQt5.QtWidgets import *
from RemoteDesign import *
from PyQt5.QtGui import QPixmap

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        image = QPixmap('channels/remote off.png')
        self.ImageLabel.setPixmap(image)
        self.VolumeSlider.setDisabled(True)


        self.PowerButton.clicked.connect(lambda: self.power())
        self.MuteButton.clicked.connect(lambda: self.mute())
        self.ChannelUpButton.clicked.connect(lambda: self.channel_up())
        self.ChannelDownButton.clicked.connect(lambda: self.channel_down())
        self.VolumeUpButton.clicked.connect(lambda: self.volume_up())
        self.VolumeDownButton.clicked.connect(lambda: self.volume_down())


    def power(self):
        if self.__status == False:
            self.__status = True
            self.screen_control()
            if self.__muted == False:
                self.VolumeSlider.setDisabled(False)

        else:
            self.__status = False
            self.VolumeSlider.setDisabled(True)
            self.screen_control()

    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.VolumeSlider.setDisabled(True)
            else:
                self.__muted = False
                self.VolumeSlider.setDisabled(False)

    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
                self.screen_control()
            else:
                self.__channel += 1
                self.screen_control()

    def channel_down(self):
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
                self.screen_control()
            else:
                self.__channel -= 1
                self.screen_control()

    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.VolumeSlider.setDisabled(False)
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.VolumeSlider.setValue(self.__volume)

    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.VolumeSlider.setDisabled(False)
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.VolumeSlider.setValue(self.__volume)

    def screen_control(self):
        if self.__status == True:
            image = QPixmap('channels/channel_' + str(self.__channel) + '.png')
            self.ImageLabel.setPixmap(image)
        else:
            image = QPixmap('channels/remote off.png')
            self.ImageLabel.setPixmap(image)


