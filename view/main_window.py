# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1126, 732)
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
        self.ENC_1_Position.setGeometry(QtCore.QRect(0, 40, 171, 41))
        self.ENC_1_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_1_Position.setDigitCount(8)
        self.ENC_1_Position.setObjectName("ENC_1_Position")
        self.ENC_3_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_3_Position.setGeometry(QtCore.QRect(380, 40, 171, 41))
        self.ENC_3_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_3_Position.setDigitCount(8)
        self.ENC_3_Position.setObjectName("ENC_3_Position")
        self.ENC_2_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_2_Position.setGeometry(QtCore.QRect(190, 40, 171, 41))
        self.ENC_2_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_2_Position.setDigitCount(8)
        self.ENC_2_Position.setObjectName("ENC_2_Position")
        self.ENC_4_Position = QtWidgets.QLCDNumber(self.centralwidget)
        self.ENC_4_Position.setGeometry(QtCore.QRect(570, 40, 171, 41))
        self.ENC_4_Position.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.ENC_4_Position.setDigitCount(8)
        self.ENC_4_Position.setObjectName("ENC_4_Position")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, -10, 161, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, -10, 151, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, -10, 161, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.ConnectToOmronBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn.setGeometry(QtCore.QRect(0, 190, 171, 51))
        self.ConnectToOmronBtn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn.setObjectName("ConnectToOmronBtn")
        self.Error_Pos_AD = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AD.setGeometry(QtCore.QRect(190, 130, 171, 41))
        self.Error_Pos_AD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AD.setDigitCount(8)
        self.Error_Pos_AD.setObjectName("Error_Pos_AD")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.Error_Pos_AB = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AB.setGeometry(QtCore.QRect(0, 130, 171, 41))
        self.Error_Pos_AB.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AB.setDigitCount(8)
        self.Error_Pos_AB.setObjectName("Error_Pos_AB")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 90, 161, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.Error_Pos_AC = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_Pos_AC.setGeometry(QtCore.QRect(380, 130, 171, 41))
        self.Error_Pos_AC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);")
        self.Error_Pos_AC.setDigitCount(8)
        self.Error_Pos_AC.setObjectName("Error_Pos_AC")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 90, 161, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.ConnectToOmronBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_2.setGeometry(QtCore.QRect(0, 250, 171, 51))
        self.ConnectToOmronBtn_2.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.ConnectToOmronBtn_2.setObjectName("ConnectToOmronBtn_2")
        self.ConnectToOmronBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_3.setGeometry(QtCore.QRect(0, 310, 171, 51))
        self.ConnectToOmronBtn_3.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_3.setObjectName("ConnectToOmronBtn_3")
        self.ConnectToOmronBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_4.setGeometry(QtCore.QRect(0, 370, 171, 51))
        self.ConnectToOmronBtn_4.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_4.setObjectName("ConnectToOmronBtn_4")
        self.ConnectToOmronBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_5.setGeometry(QtCore.QRect(0, 430, 171, 51))
        self.ConnectToOmronBtn_5.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_5.setObjectName("ConnectToOmronBtn_5")
        self.ConnectToOmronBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectToOmronBtn_6.setGeometry(QtCore.QRect(0, 490, 171, 51))
        self.ConnectToOmronBtn_6.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);")
        self.ConnectToOmronBtn_6.setObjectName("ConnectToOmronBtn_6")
        self.ferq_lab = QtWidgets.QLCDNumber(self.centralwidget)
        self.ferq_lab.setGeometry(QtCore.QRect(570, 130, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(3)
        self.ferq_lab.setFont(font)
        self.ferq_lab.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 255);\n"
"font: 25 italic 48pt \"Ubuntu\";")
        self.ferq_lab.setDigitCount(8)
        self.ferq_lab.setProperty("value", 20.0)
        self.ferq_lab.setObjectName("ferq_lab")
        self.ferq_decriment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ferq_decriment_btn.setGeometry(QtCore.QRect(180, 250, 181, 51))
        self.ferq_decriment_btn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.ferq_decriment_btn.setObjectName("ferq_decriment_btn")
        self.ferq_increment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ferq_increment_btn.setGeometry(QtCore.QRect(180, 190, 181, 51))
        self.ferq_increment_btn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.ferq_increment_btn.setObjectName("ferq_increment_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 90, 161, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.log_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.log_box.setGeometry(QtCore.QRect(370, 550, 741, 111))
        self.log_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.502, y1:0.0223636, x2:0.597, y2:0.994318, stop:0 rgba(90, 93, 92, 255), stop:1 rgba(255, 255, 255, 255));")
        self.log_box.setObjectName("log_box")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(180, 550, 181, 51))
        self.start_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(22, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(180, 610, 181, 51))
        self.stop_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.stop_btn.setObjectName("stop_btn")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(760, 0, 181, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.axis_a_vel_box = QtWidgets.QLCDNumber(self.centralwidget)
        self.axis_a_vel_box.setGeometry(QtCore.QRect(760, 40, 171, 41))
        self.axis_a_vel_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.axis_a_vel_box.setDigitCount(8)
        self.axis_a_vel_box.setObjectName("axis_a_vel_box")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(960, 0, 181, 31))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.axis_b_vel_box = QtWidgets.QLCDNumber(self.centralwidget)
        self.axis_b_vel_box.setGeometry(QtCore.QRect(950, 40, 161, 41))
        self.axis_b_vel_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.axis_b_vel_box.setDigitCount(8)
        self.axis_b_vel_box.setObjectName("axis_b_vel_box")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(760, 90, 181, 31))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.axis_c_vel_box = QtWidgets.QLCDNumber(self.centralwidget)
        self.axis_c_vel_box.setGeometry(QtCore.QRect(760, 130, 171, 41))
        self.axis_c_vel_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.axis_c_vel_box.setDigitCount(8)
        self.axis_c_vel_box.setObjectName("axis_c_vel_box")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(950, 90, 181, 31))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.axis_d_vel_box = QtWidgets.QLCDNumber(self.centralwidget)
        self.axis_d_vel_box.setGeometry(QtCore.QRect(950, 130, 161, 41))
        self.axis_d_vel_box.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.457014, y1:0.511, x2:1, y2:0.494318, stop:0 rgba(72, 120, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.axis_d_vel_box.setDigitCount(8)
        self.axis_d_vel_box.setObjectName("axis_d_vel_box")
        self.power_enable_btn = QtWidgets.QPushButton(self.centralwidget)
        self.power_enable_btn.setGeometry(QtCore.QRect(0, 550, 171, 51))
        self.power_enable_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(22, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.power_enable_btn.setObjectName("power_enable_btn")
        self.power_disable_btn = QtWidgets.QPushButton(self.centralwidget)
        self.power_disable_btn.setGeometry(QtCore.QRect(0, 610, 171, 51))
        self.power_disable_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00878733, y1:0.528045, x2:1, y2:0.545, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.power_disable_btn.setObjectName("power_disable_btn")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 310, 931, 221))
        self.widget.setObjectName("widget")
        self.clear_error_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_error_btn.setGeometry(QtCore.QRect(380, 190, 181, 51))
        self.clear_error_btn.setStyleSheet("background-color: rgb(126, 83, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.clear_error_btn.setObjectName("clear_error_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 31))
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
        self.ferq_decriment_btn.setText(_translate("MainWindow", "-"))
        self.ferq_increment_btn.setText(_translate("MainWindow", "+"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Set ferquency</p></body></html>"))
        self.log_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.start_btn.setText(_translate("MainWindow", "START"))
        self.stop_btn.setText(_translate("MainWindow", "STOP"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Ferquency<span style=\" font-size:14pt;\"> A (Hz)</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Ferquency<span style=\" font-size:14pt;\"> B (Hz)</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Ferquency<span style=\" font-size:14pt;\"> C (Hz)</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Ferquency<span style=\" font-size:14pt;\"> D (Hz)</span></p></body></html>"))
        self.power_enable_btn.setText(_translate("MainWindow", "Enable AC"))
        self.power_disable_btn.setText(_translate("MainWindow", "Disable AC"))
        self.clear_error_btn.setText(_translate("MainWindow", "Clear errors"))
from pyqtgraph import PlotWidget
