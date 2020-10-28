import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import view # Это наш конвертированный файл дизайна

import sched, time
import threading 

import external_devices.controller.omron_nx as Omron




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('view/main.ui', self)
        
        #self.ConnectToOmronBtn.clicked.connect(self.ConnectToOmron)
        #self.ConnectToOmronBtn_2.clicked.connect(self.Start)
    

      
       # self.TimerUpdate   = Timer(1, self.UpdateValues)
    '''
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
'''
timer          = QTimer()
UPDATE_TIME_MS = 50
import json
def read_config():
    try :
        config_file   = open('config/client_config.json' , 'r')
        cohfig_data   = config_file.read()
        return json.loads(cohfig_data)
    except Exception as e:
        print(str(e)) 

def main():
      
    app  = QtWidgets.QApplication(sys.argv) 
    main           = MainWindow()  

    cOmron = Omron.omronNx(read_config(), main, UPDATE_TIME_MS)
    main.ConnectToOmronBtn.clicked.connect(cOmron.connect)
    timer.timeout.connect(cOmron.update)
    timer.start(UPDATE_TIME_MS)

    main.show()  
    app.exec_()  

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()