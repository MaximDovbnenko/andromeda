# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1292, 839)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ENC_1_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_1_Position.setGeometry(QtCore.QRect(0, 40, 291, 61))
        self.ENC_1_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_1_Position.setDigitCount(8)
        self.ENC_1_Position.setObjectName("ENC_1_Position")
        self.ENC_3_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_3_Position.setGeometry(QtCore.QRect(0, 280, 291, 61))
        self.ENC_3_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_3_Position.setDigitCount(8)
        self.ENC_3_Position.setObjectName("ENC_3_Position")
        self.ENC_2_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_2_Position.setGeometry(QtCore.QRect(0, 160, 291, 61))
        self.ENC_2_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_2_Position.setDigitCount(8)
        self.ENC_2_Position.setObjectName("ENC_2_Position")
        self.ENC_4_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_4_Position.setGeometry(QtCore.QRect(0, 400, 291, 61))
        self.ENC_4_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_4_Position.setDigitCount(8)
        self.ENC_4_Position.setObjectName("ENC_4_Position")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 161, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 151, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 161, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.ConnectToOmronBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn.setGeometry(QtCore.QRect(0, 480, 291, 51))
        self.ConnectToOmronBtn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn.setObjectName("ConnectToOmronBtn")
        self.Error_Pos_AD = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AD.setGeometry(QtCore.QRect(300, 160, 261, 61))
        self.Error_Pos_AD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AD.setDigitCount(8)
        self.Error_Pos_AD.setObjectName("Error_Pos_AD")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 0, 161, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.Error_Pos_AB = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AB.setGeometry(QtCore.QRect(300, 40, 261, 61))
        self.Error_Pos_AB.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AB.setDigitCount(8)
        self.Error_Pos_AB.setObjectName("Error_Pos_AB")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 240, 161, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.Error_Pos_AC = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AC.setGeometry(QtCore.QRect(300, 280, 261, 61))
        self.Error_Pos_AC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AC.setDigitCount(8)
        self.Error_Pos_AC.setObjectName("Error_Pos_AC")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 120, 161, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.ConnectToOmronBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_2.setGeometry(QtCore.QRect(0, 540, 131, 71))
        self.ConnectToOmronBtn_2.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.ConnectToOmronBtn_2.setObjectName("ConnectToOmronBtn_2")
        self.ConnectToOmronBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_3.setGeometry(QtCore.QRect(160, 540, 131, 71))
        self.ConnectToOmronBtn_3.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_3.setObjectName("ConnectToOmronBtn_3")
        self.ConnectToOmronBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_4.setGeometry(QtCore.QRect(0, 620, 131, 71))
        self.ConnectToOmronBtn_4.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_4.setObjectName("ConnectToOmronBtn_4")
        self.ConnectToOmronBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_5.setGeometry(QtCore.QRect(160, 620, 131, 71))
        self.ConnectToOmronBtn_5.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_5.setObjectName("ConnectToOmronBtn_5")
        self.ConnectToOmronBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_6.setGeometry(QtCore.QRect(0, 700, 291, 61))
        self.ConnectToOmronBtn_6.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_6.setObjectName("ConnectToOmronBtn_6")
        self.Ferq_lab = QtWidgets.QLCDNumber(self.centralwidget)
        self.Ferq_lab.setGeometry(QtCore.QRect(580, 40, 261, 181))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(3)
        self.Ferq_lab.setFont(font)
        self.Ferq_lab.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 255);\n"
"font: 25 italic 48pt \"Ubuntu\";")
        self.Ferq_lab.setDigitCount(8)
        self.Ferq_lab.setProperty("value", 20.0)
        self.Ferq_lab.setObjectName("Ferq_lab")
        self.Ferq_plus_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Ferq_plus_minus.setGeometry(QtCore.QRect(580, 230, 121, 111))
        self.Ferq_plus_minus.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Ferq_plus_minus.setObjectName("Ferq_plus_minus")
        self.Ferq_plus_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Ferq_plus_btn.setGeometry(QtCore.QRect(720, 230, 121, 111))
        self.Ferq_plus_btn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Ferq_plus_btn.setObjectName("Ferq_plus_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 0, 161, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(850, 40, 431, 721))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.502, y1:0.0223636, x2:0.597, y2:0.994318, stop:0 rgba(90, 93, 92, 255), stop:1 rgba(255, 255, 255, 255));")
        self.textBrowser.setObjectName("textBrowser")
        self.Start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Start_btn.setGeometry(QtCore.QRect(300, 620, 261, 141))
        self.Start_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(22, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.Start_btn.setObjectName("Start_btn")
        self.Stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_btn.setGeometry(QtCore.QRect(570, 620, 261, 141))
        self.Stop_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.Stop_btn.setObjectName("Stop_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Position A (deg)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Position B (deg)</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Position C (deg)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Position D (deg)</span></p></body></html>"))
        self.ConnectToOmronBtn.setText(_translate("MainWindow", "Connect OPC UA"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Error A - B (deg)</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Error A - D (deg)</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Error A - C (deg)</span></p></body></html>"))
        self.ConnectToOmronBtn_2.setText(_translate("MainWindow", "Home A"))
        self.ConnectToOmronBtn_3.setText(_translate("MainWindow", "Home B"))
        self.ConnectToOmronBtn_4.setText(_translate("MainWindow", "Home C"))
        self.ConnectToOmronBtn_5.setText(_translate("MainWindow", "Home D"))
        self.ConnectToOmronBtn_6.setText(_translate("MainWindow", "Home All"))
        self.Ferq_plus_minus.setText(_translate("MainWindow", "-"))
        self.Ferq_plus_btn.setText(_translate("MainWindow", "+"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Ferquency</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Start_btn.setText(_translate("MainWindow", "START"))
        self.Stop_btn.setText(_translate("MainWindow", "STOP"))
