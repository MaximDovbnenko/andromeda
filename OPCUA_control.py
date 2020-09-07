
from opcua import Client
from opcua import ua
import ReadConfig

class OpcUaControl:
    def __init__(self):
        self.ControlItemList = ReadConfig.FileNodeItemList()
        self.ControlItemList.createListFromFile()
        self.CurrentClient = Client("opc.tcp://192.168.250.1:4840")
        pass

