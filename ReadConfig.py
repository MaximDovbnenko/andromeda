'''
Чтение файла конфигурации 
'''
class FileNodeItem:
    def __init__(self):
        self.Key      = ""
        self.Value    = ""
        self.ReadOnly = False
        self.Update   = True
    @staticmethod
    def Parse(line):
        #input string format  Key : Value : ReadOnly : Update  
        #For example          HomeMotorA : n = 4; s = 15 : False : True
        args = line.split(":")
        retObject = FileNodeItem()
        if(len(args) == 4):
            retObject.Key   = args[0].strip()
            retObject.Value = args[1].strip()
        print(retObject.ToString())
        return retObject

    def ToString(self):
        return "Key: " + self.Key + " Value: " + self.Value

class FileNodeItemList:
    def __init__(self):
        self.NodeList = []
    
    def getNodeByName(self, key):
        for node in self.NodeList:
            if(isinstance(node, FileNodeItem)):
                if( node.Key == key):
                    return node.Value

    def createListFromFile(self, path = "cfg/config.ini"):
        fileConfig = open(path, 'r')
        for line in fileConfig:
            self.NodeList.append(
                FileNodeItem.Parse(line)
            )
        pass
    def getLength(self):
        return len(self.NodeList)
    