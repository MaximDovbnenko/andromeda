
from opcua import Client
from opcua import ua

import external_devices.drives.RD88 as RD88
import external_devices.controller.plc as plc
import external_devices.drives.motor_poll as MPoll

class omronNx:
    def __init__(self, config_json, qt_main_ui, time_update):
        self._qt_main_ui    = qt_main_ui
        self._config_json   = config_json
        self.time_update    = time_update
        self.PLC            = plc.PLC(config_json, qt_main_ui, self)
        self.connect_addres = None
        self.opc_ua_client  = None
        self.Time           = 0
        self.F              = 20
        self.Drivers        = MPoll.MotorsPoll(config_json, qt_main_ui, self)

        self.is_stop  = False
        self.is_opcua_connected = False

        self.is_started_drivers = False
        self.read_config()
        self.create_opc_client()
        self.init_ui_signals()

        self.count_update = 0
        

    def init_ui_signals(self):
        self._qt_main_ui.ConnectToOmronBtn.clicked.connect(self.connect)
        
    def create_opc_client(self):
        self.opc_ua_client  = Client(
            self.connect_addres
        )
    def connect(self):
        try:
            self.opc_ua_client.connect()
            self.add_to_log_box("connect to : {}".format(self.connect_addres))
            self.is_opcua_connected = True
        except Exception as e:
            self.is_opcua_connected = True
            self.add_to_log_box("connection error : {}".format(str(e)))
            #self.PLC._set_alarm_on();

        

    def update(self):
        self.Drivers.update()
        self.view_update()
        self.PLC.update()
       

        pass

    def view_update(self):
        self._qt_main_ui.ferq_lab.display(self.F)
        pass


    def read_config(self):
        try:
            self.connect_addres = self._config_json["network"][0]["opc_addr"]
        except Exception as e:
            self.add_to_log_box(str(e))


    def get_value(self, cmd):
        pass

    def set_value(self, node, value):
        try :
            node = self.opc_ua_client.get_node(node)
            node.set_attribute(ua.AttributeIds.Value, ua.DataValue(value))
        except Exception as e:
            self.add_to_log_box("set_value error : {}".format(str(e)))
        pass

    def add_to_log_box(self, text):
        tmp_text =  "" #self._qt_main_ui.log_box.text
        self._qt_main_ui.log_box.setText(tmp_text + "\n" +text)
        pass
      