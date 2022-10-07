import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import QRc
import sys
import urllib.request
import pytube
import pafy


class Ui_Dialog(QMainWindow):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(853, 455)
        Dialog.setStyleSheet("QMainWindow{\n"
                             "background-color: #ccc;\n"
                             "}")
        self.label_quality = QtWidgets.QLabel(Dialog)
        self.label_quality.setGeometry(QtCore.QRect(180, 356, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_quality.setFont(font)
        self.label_quality.setStyleSheet("QLabel{\n"
                                         "color: #fff;\n"
                                         "}")
        self.label_quality.setObjectName("label_quality")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(130, -10, 751, 471))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 200, 641, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "padding: 4px 8px;\n"
                                    "font-size : 12px;\n"
                                    "color: #000;\n"
                                    "background-color: #fff;\n"
                                    "border: 1px solid #ccc;\n"
                                    "border-radius: 15px;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 250, 511, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 12px;\n"
                                      "color: #000;\n"
                                      "background-color: #fff;\n"
                                      "border: 1px solid #ccc;\n"
                                      "border-radius: 15px;\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(530, 250, 121, 31))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: #55f ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color: #001ab1 ;\n"
                                        "}")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 300, 641, 31))
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
                                       "background-color: #55f ;\n"
                                       "margin: 0px ;\n"
                                       "border-radius:15px;\n"
                                       "}\n"
                                       "QProgressBar{\n"
                                       "background-color: #cccccc ;\n"
                                       "border-radius:15px;\n"
                                       "}")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 390, 141, 41))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: #55f ;\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color: #001ab1 ;\n"
                                        "}")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(200, 60, 251, 131))
        self.label_5.setStyleSheet("image: url(:/folder.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 270, 641, 31))
        self.progressBar_2.setStyleSheet("QProgressBar::chunk{\n"
                                         "background-color: #55f ;\n"
                                         "margin: 0px ;\n"
                                         "border-radius:15px;\n"
                                         "}\n"
                                         "QProgressBar{\n"
                                         "background-color: #ccc ;\n"
                                         "border-radius:15px;\n"
                                         "}")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 170, 511, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 12px;\n"
                                      "color: #000;\n"
                                      "background-color: #fff;\n"
                                      "border: 1px solid #ccc;\n"
                                      "border-radius: 15px;\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 220, 511, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 12px;\n"
                                      "color: #000;\n"
                                      "background-color: #fff;\n"
                                      "border: 1px solid #ccc;\n"
                                      "border-radius: 15px;\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(210, 30, 251, 131))
        self.label_6.setStyleSheet("image: url(:/video-player(1).png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 220, 121, 31))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: #55f ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:#001ab1 ;\n"
                                        "}")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 380, 191, 41))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: #55f ;\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:#001ab1;\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/video-player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 170, 121, 31))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: #55f ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color: #001ab1 ;\n"
                                        "}")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(318, 320, 331, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(80, 320, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 380, 191, 40))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "padding: 4px 8px;\n"
                                         "font-size : 14px;\n"
                                         "color: #fff;\n"
                                         "background-color: #55f ;\n"
                                         "border-radius: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "color: #fff;\n"
                                         "background-color: #001ab1 ;\n"
                                         "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 360, 141, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "padding: 4px 8px;\n"
                                         "font-size : 14px;\n"
                                         "color: #fff;\n"
                                         "background-color: #55f ;\n"
                                         "border-radius: 20px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "color: #fff;\n"
                                         "background-color:#001ab1 ;\n"
                                         "}")
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 240, 511, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 12px;\n"
                                      "color: #000;\n"
                                      "background-color: #fff;\n"
                                      "border: 1px solid #ccc;\n"
                                      "border-radius: 15px;\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 300, 641, 31))
        self.progressBar_3.setStyleSheet("QProgressBar::chunk{\n"
                                         "background-color: #55f ;\n"
                                         "margin: 0px ;\n"
                                         "border-radius:15px;\n"
                                         "}\n"
                                         "QProgressBar{\n"
                                         "background-color: #ccc ;\n"
                                         "border-radius:15px;\n"
                                         "}")
        self.progressBar_3.setMaximum(100)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(210, 50, 251, 131))
        self.label_9.setStyleSheet("image: url(:/playlist.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 190, 641, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 12px;\n"
                                      "color: #000;\n"
                                      "background-color: #fff;\n"
                                      "border: 1px solid #ccc;\n"
                                      "border-radius: 15px;\n"
                                      "}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 240, 121, 31))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "padding: 4px 8px;\n"
                                         "font-size : 14px;\n"
                                         "color: #fff;\n"
                                         "background-color: #55f ;\n"
                                         "border-radius: 15px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "color: #fff;\n"
                                         "background-color: #001ab1 ;\n"
                                         "}")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_9.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_10.raise_()
        self.progressBar_3.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_12.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 71, 71))
        self.label_8.setStyleSheet("image: url(:/language.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(80, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setLineWidth(-1)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 81, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "padding: 4px 8px;\n"
                                      "font-size : 14px;\n"
                                      "color: #fff;\n"
                                      "background-color: rgb(118, 118, 118) ;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "color: #fff;\n"
                                      "background-color:rgb(2, 200, 255) ;\n"
                                      "}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 330, 81, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: none ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:rgb(2, 200, 255) ;\n"
                                        "}")
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xcvbh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 230, 81, 71))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: none ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:rgb(2, 200, 255) ;\n"
                                        "}")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/playlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 101, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 400, 81, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 81, 71))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "padding: 4px 8px;\n"
                                        "font-size : 14px;\n"
                                        "color: #fff;\n"
                                        "background-color: none ;\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: #fff;\n"
                                        "background-color:rgb(2, 200, 255) ;\n"
                                        "}")
        self.pushButton_4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/video-player(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_quality.setText(_translate("Dialog", "Choose Quality"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter link here"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Click browse button to choose the save location"))
        self.pushButton_5.setText(_translate("Dialog", "Browse"))
        self.pushButton_6.setText(_translate("Dialog", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "files"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Enter link here"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Click browse button to choose the save location"))
        self.pushButton_7.setText(_translate("Dialog", "Browse"))
        self.pushButton_8.setText(_translate("Dialog", "Download video"))
        self.pushButton_9.setText(_translate("Dialog", "ok"))
        self.label_7.setText(_translate("Dialog", "Choose quality"))
        self.pushButton_11.setText(_translate("Dialog", "Download audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "videos"))
        self.pushButton_10.setText(_translate("Dialog", "Download"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Click browse button to choose the save location"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Enter link here"))
        self.pushButton_12.setText(_translate("Dialog", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "playlist"))
        self.label_10.setText(_translate("Dialog", "Choose the language"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "English"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "العربية"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "settings"))
        self.label.setText(_translate("Dialog", "Download file"))
        self.label_2.setText(_translate("Dialog", "Download video"))
        self.label_3.setText(_translate("Dialog", "Download Playlist"))
        self.label_4.setText(_translate("Dialog", "Settings"))





class Test(Ui_Dialog):
        def __init__(self):
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.setFixedSize(851, 455)
            self.progressBar_3.hide()
            self.progressBar_2.hide()
            self.comboBox.hide()
            self.label_7.hide()
            self.pushButton_11.hide()
            self.tabWidget.setCurrentIndex(0)
            self.setWindowTitle("Abdellah")
            self.icon = QIcon("D:/d.ico")
            self.setWindowIcon(self.icon)

            self.pushButton.clicked.connect(self.TAB)
            self.pushButton_4.clicked.connect(self.TAB_2)
            self.pushButton_3.clicked.connect(self.TAB_3)
            self.pushButton_2.clicked.connect(self.TAB_4)
            self.comboBox_2.currentIndexChanged.connect(self.translate)
            self.pushButton_5.clicked.connect(self.Broswe_file)
            self.pushButton_6.clicked.connect(self.Download_Files)
            self.pushButton_9.clicked.connect(self.Get_Video_Data)
            self.pushButton_8.clicked.connect(self.Download_Video)
            self.pushButton_7.clicked.connect(self.Browse)
            self.pushButton_10.clicked.connect(self.Download_Playlist)
            self.pushButton_12.clicked.connect(self.Browse)
            self.tabWidget.currentChanged.connect(self.shadow)




        def shadow(self):
            i = self.tabWidget.currentIndex()
            if i == 0:
                self.pushButton.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: #767676 ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_3.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_2.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
            elif i == 1:
                self.pushButton.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color:none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: #767676 ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_3.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_2.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
            elif i == 2:
                self.pushButton.setStyleSheet("QPushButton{\n"
                                              "padding: 4px 8px;\n"
                                              "font-size : 14px;\n"
                                              "color: #fff;\n"
                                              "background-color: none ;\n"
                                              "border-radius: 15px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "color: #fff;\n"
                                              "background-color:rgb(2, 200, 255) ;\n"
                                              "}")
                self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_3.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: #767676 ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_2.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
            elif i == 3:
                self.pushButton.setStyleSheet("QPushButton{\n"
                                              "padding: 4px 8px;\n"
                                              "font-size : 14px;\n"
                                              "color: #fff;\n"
                                              "background-color: none ;\n"
                                              "border-radius: 15px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "color: #fff;\n"
                                              "background-color:rgb(2, 200, 255) ;\n"
                                              "}")
                self.pushButton_4.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_3.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: none ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")
                self.pushButton_2.setStyleSheet("QPushButton{\n"
                                                "padding: 4px 8px;\n"
                                                "font-size : 14px;\n"
                                                "color: #fff;\n"
                                                "background-color: #767676 ;\n"
                                                "border-radius: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "color: #fff;\n"
                                                "background-color:rgb(2, 200, 255) ;\n"
                                                "}")

        def TAB(self):
            self.tabWidget.setCurrentIndex(0)
        def TAB_2(self):
            self.tabWidget.setCurrentIndex(1)
        def TAB_3(self):
            self.tabWidget.setCurrentIndex(2)
        def TAB_4(self):
            self.tabWidget.setCurrentIndex(3)


        def translate(self):
            index = int(self.comboBox_2.currentIndex())

            if index == 0:
                self.lineEdit.setPlaceholderText("Enter link here")
                self.lineEdit_2.setPlaceholderText("Click browse button to choose the save location")
                self.pushButton_5.setText("Browse")
                self.pushButton_6.setText("Download")
                self.label.setText("Download file")
                self.lineEdit_3.setPlaceholderText("Enter link here")
                self.lineEdit_4.setPlaceholderText("Click browse button to choose the save location")
                self.pushButton_11.setText("Download audio")
                self.pushButton_7.setText("Browse")
                self.label_7.setText("Choose quality")
                self.pushButton_9.setText("ok")
                self.pushButton_8.setText("Download video")
                self.label_2.setText("Download video")
                self.lineEdit_6.setPlaceholderText("Enter link here")
                self.lineEdit_5.setPlaceholderText("Click browse button to choose the save location")
                self.pushButton_12.setText("Browse")
                self.pushButton_10.setText("Download")
                self.label_3.setText("Download Playlist")
                self.label_10.setText("Choose the language")
                self.label_4.setText("Settings")

            elif index == 1:
                self.lineEdit.setPlaceholderText("أدخل الرابط")
                self.lineEdit_2.setPlaceholderText("اضغط زر التصفح لتحديد موقع التخزين")
                self.pushButton_5.setText("تصفح")
                self.pushButton_6.setText("تحميل")
                self.label.setText("تحميل ملف")
                self.lineEdit_3.setPlaceholderText("أدخل الرابط")
                self.lineEdit_4.setPlaceholderText("اضغط زر التصفح لتحديد موقع التخزين")
                self.pushButton_8.setText("تحميل الفيديو")
                self.pushButton_7.setText("تصفح")
                self.label_7.setText("اختر الجودة")
                self.pushButton_9.setText("موافق")
                self.pushButton_11.setText("تحميل الصوت")
                self.label_2.setText("تحميل فيديو")
                self.lineEdit_6.setPlaceholderText("أدخل الرابط")
                self.lineEdit_5.setPlaceholderText("اضغط زر التصفح لتحديد موقع التخزين")
                self.pushButton_12.setText("تصفح")
                self.pushButton_10.setText("تحميل")
                self.label_3.setText("تحميل قائمة تشغيل")
                self.label_10.setText("اختر اللغة")
                self.label_4.setText("الإعدادات")

        def Browse(self):
            tab_index = int(self.tabWidget.currentIndex())
            self.save_loc = QFileDialog.getExistingDirectory(self, "Select Download Directory")
            if tab_index == 1:
                self.lineEdit_4.setText(self.save_loc)
            elif tab_index == 2:
                self.lineEdit_5.setText(self.save_loc)

        def Broswe_file(self):
            save = QFileDialog.getSaveFileName(self, caption="Save as", directory=".", filter="All Files(*.*)")
            self.lineEdit_2.setText(str(save[0]))

        def Report(self, Blocknum, Blocksize, totalsize):
            percent = Blocknum * Blocksize

            if totalsize > 0:
                report = percent * 100 / totalsize
                self.progressBar.setValue(int(report))
                QApplication.processEvents()


        def Download_Files(self):
            url = self.lineEdit.text()
            save_location = self.lineEdit_2.text()

            try:
                urllib.request.urlretrieve(url, save_location, self.Report)
            except Exception as y:
                QMessageBox.warning(self, "Failed", str(y))
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.progressBar.setValue(0)
                return
            self.progressBar.setValue(100)
            QMessageBox.information(self, "information", "The Download is complete")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.progressBar.setValue(0)

########################################## Download video from youtube ###########################
        def Get_Video_Data(self):
            try:
                self.url_video = self.lineEdit_3.text()
                self.video = pafy.new(self.url_video)
                self.stream = self.video.streams
                for item in self.stream:
                    data = "{} {}".format(item.extension, item.quality)
                    self.comboBox.addItem(data)
                    self.comboBox.show()
                    self.label_7.show()
            except Exception as v:
                QMessageBox.warning(self, "Failed", str(v))
        def Download_Video(self):
            try:
                save = self.lineEdit_4.text()
                self.stream[int(self.comboBox.currentIndex())].download(filepath=save)
            except Exception as x:
                QMessageBox.warning(self, "Failed", str(x))
                self.comboBox.clear()
                self.lineEdit_3.setText("")
                self.lineEdit_4.setText("")
                self.comboBox.hide()
                self.label_7.hide()
                return
            QMessageBox.information(self, "Complete", "The download complete")
            self.comboBox.clear()
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.comboBox.hide()
            self.label_7.hide()
########################################################################################


########################## Download playlist from youtube ##############################
        def Download_Playlist(self):
            try:

                try:
                    url, save_location = self.lineEdit_6.text(), self.lineEdit_5.text()
                    
                    play_list = pytube.Playlist(url)
                
                    for video in play_list.videos:
                        video.streams.get_highest_resolution().download(output_path=save_location)
                    # self.video = pafy.new(url)
                    # self.stream = self.video.streams
                    # self.stream[0].download(filepath=save_location)
                except Exception as v:
                    QMessageBox.warning(self, "Failed", str(v))


                # playlist = pafy.get_playlist2(url)
                
                # playlist['items'][21]['pafy'].getbest()


            except Exception as p:
                QMessageBox.warning(self, "Failed", str(p))
                self.lineEdit_6.setText("")
                self.lineEdit_5.setText("")
                return
            QMessageBox.information(self, "Complete", "The download complete")
            self.lineEdit_6.setText("")
            self.lineEdit_5.setText("")
##########################################################################################


app = QApplication(sys.argv)
window = Test()
window.show()
app.exec_()