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

class SimulationOmron:
    def __init__(self):
        self.PositionA = 0
        self.PositionB = 0
        self.PositionC = 0
        self.PositionD = 0
        self.Threshold = 10
        self.va = 10.1
        self.vb = 10.1
        self.vc = 10.1
        self.vd = 10.1
    def SetVelByAxis(self, axis, vel):
        if(axis == 'a' or axis == 'A'):
            self.va = vel
        elif(axis == 'b' or axis == 'B'):
            self.vb = vel
        elif(axis == 'c' or axis == 'C'):
            self.vc = vel
        elif(axis == 'd' or axis == 'D'):
            self.vd = vel
        else:
            print('Axis ' + str(axis) + " not exist!")
    def Update(self):
        rnd_A = random.random() * 100
        if rnd_A > self.Threshold:
            self.PositionA = self.PositionA +  self.va
        rnd_B = random.random() * 100
        if rnd_B > self.Threshold:
            self.PositionB = self.PositionB +  self.vb

        rnd_C = random.random() * 100
        if rnd_C > self.Threshold:
            self.PositionC = self.PositionC +  self.vc
        
        rnd_D = random.random() * 100
        if rnd_D > self.Threshold:
            self.PositionD = self.PositionD +  self.vd

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
        self.CurrentClient.connect()
        self.Sim = SimulationOmron()
      
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
        self.ENC_2_Position.display (round(self.Sim.PositionB, 1))
        self.ENC_3_Position.display (round(self.Sim.PositionC, 1))
        self.ENC_4_Position.display (round(self.Sim.PositionD, 1))
        
        self.ErrorAB = self.Sim.PositionA - self.Sim.PositionB
        self.ErrorAC = self.Sim.PositionA - self.Sim.PositionC
        self.ErrorAD = self.Sim.PositionA - self.Sim.PositionD

        self.Error_Pos_AB.display (round(self.ErrorAB, 1))
        self.Error_Pos_AC.display (round(self.ErrorAC, 1))
        self.Error_Pos_AD.display (round(self.ErrorAD, 1))

        if self.EnableControlA.isChecked():
            self.Sim.SetVelByAxis('B', self.ErrorAB * 0.8 )
        if self.EnableControlB.isChecked():
            self.Sim.SetVelByAxis('C', self.ErrorAC * 0.8 )
        if self.EnableControlC.isChecked():
            self.Sim.SetVelByAxis('D', self.ErrorAD * 0.8 )
        #self.TimerTick.enter(0.5, 1, self.UpdateValues, (self.TimerTick,))
        pass
    def ConnectToOmron(self):
        self.CurrentClient.connect()
        root =  self.CurrentClient.get_root_node()
        pass

def tick():
    print("tick")
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