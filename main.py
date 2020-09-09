import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import main_window  # Это наш конвертированный файл дизайна
from opcua import Client
from opcua import ua
import sched, time
import threading 
import simulation
import math
import random
import OPCUA_control



class ExampleApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.S = False
        self.Controller = OPCUA_control.OpcUaControl()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        self.ConnectToOmronBtn.clicked.connect(self.ConnectToOmron)
        self.ConnectToOmronBtn_2.clicked.connect(self.Start)
        self.CurrentClient = Client("opc.tcp://192.168.250.1:4840")

      
       # self.TimerUpdate   = Timer(1, self.UpdateValues)

    def Start(self):
         self.S = not self.S
         print(self.S)
         ENC_A = self.CurrentClient.get_node("ns=4;s=Start")
         ENC_A.set_attribute(ua.AttributeIds.Value, ua.DataValue(not self.S))
         

    def UpdateValues(self):
        #self.Sim.Update()
        objects = self.CurrentClient.get_objects_node()
        ENC_A = self.CurrentClient.get_node("ns=4;s=N1_Ch1_Encoder_Present_Position")
        #print(ENC_A.get_value())
        self.ENC_1_Position.display (ENC_A.get_value())

      
    def ConnectToOmron(self):
        self.CurrentClient.connect()
        root =  self.CurrentClient.get_root_node()
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp

    timer = QTimer()
    timer.timeout.connect(window.UpdateValues)
    timer.start(500)

    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()