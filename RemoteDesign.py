# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoteDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 515)
        MainWindow.setMinimumSize(QtCore.QSize(472, 515))
        MainWindow.setMaximumSize(QtCore.QSize(472, 515))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 451, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.PowerButton = QtWidgets.QPushButton(self.centralwidget)
        self.PowerButton.setGeometry(QtCore.QRect(170, 310, 121, 51))
        self.PowerButton.setObjectName("PowerButton")
        self.ChannelUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChannelUpButton.setGeometry(QtCore.QRect(30, 310, 111, 61))
        self.ChannelUpButton.setObjectName("ChannelUpButton")
        self.ChannelDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChannelDownButton.setGeometry(QtCore.QRect(30, 390, 111, 61))
        self.ChannelDownButton.setObjectName("ChannelDownButton")
        self.VolumeUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.VolumeUpButton.setGeometry(QtCore.QRect(330, 310, 111, 61))
        self.VolumeUpButton.setObjectName("VolumeUpButton")
        self.VolumeDownButton = QtWidgets.QPushButton(self.centralwidget)
        self.VolumeDownButton.setGeometry(QtCore.QRect(330, 390, 111, 61))
        self.VolumeDownButton.setObjectName("VolumeDownButton")
        self.MuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.MuteButton.setGeometry(QtCore.QRect(170, 390, 121, 51))
        self.MuteButton.setObjectName("MuteButton")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(20, 20, 431, 211))
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setGeometry(QtCore.QRect(150, 460, 160, 22))
        self.VolumeSlider.setMaximum(2)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setInvertedAppearance(False)
        self.VolumeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.VolumeSlider.setTickInterval(1)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 480, 16, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 480, 21, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 480, 16, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TV Remote"))
        self.PowerButton.setText(_translate("MainWindow", "Power"))
        self.ChannelUpButton.setText(_translate("MainWindow", "Channel Up"))
        self.ChannelDownButton.setText(_translate("MainWindow", "Channel Down"))
        self.VolumeUpButton.setText(_translate("MainWindow", "Volume Up"))
        self.VolumeDownButton.setText(_translate("MainWindow", "Volume Down"))
        self.MuteButton.setText(_translate("MainWindow", "Mute"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())