
from opcua import Client
from opcua import ua

import external_devices.drives.RD88 as RD88


class omronNx:
    def __init__(self, config_json, qt_main_ui, time_update):
        self._qt_main_ui    = qt_main_ui
        self._config_json   = config_json
        self.time_update    = time_update
        self.connect_addres = None
        self.opc_ua_client  = None
        self.Time           = 0
        self.F              = 20
        self.Drivers   = []
        self.Encoders = []
        self.is_stop  = False

        self.is_started_drivers = False
        self.read_config()
        self.create_opc_client()
        self.init_drivers()
        self.init_ui_signals()
        
    def init_drivers(self):
        self.Drivers.append(
            RD88.Rd88(
                self, 
                self._config_json["hardware_addr"]["axis_a_set_vel_addr"], 
                self._config_json["hardware_addr"]["axis_a_in_home_flag_addr"],
                0.05, 100,
                self.time_update,
                self._qt_main_ui.axis_a_vel_box
                )
        )
        self.Drivers.append(
            RD88.Rd88(
                self, 
                self._config_json["hardware_addr"]["axis_b_set_vel_addr"], 
                self._config_json["hardware_addr"]["axis_b_in_home_flag_addr"],
                0.05, 100,
                self.time_update,
                self._qt_main_ui.axis_b_vel_box
                )
        )
        self.Drivers.append(
            RD88.Rd88(
                self, 
                self._config_json["hardware_addr"]["axis_d_set_vel_addr"], 
                self._config_json["hardware_addr"]["axis_d_in_home_flag_addr"],
                0.05, 100,
                self.time_update,
                self._qt_main_ui.axis_d_vel_box
                )
        )
        self.Drivers.append(
            RD88.Rd88(
                self, 
                self._config_json["hardware_addr"]["axis_c_set_vel_addr"], 
                self._config_json["hardware_addr"]["axis_c_in_home_flag_addr"],
                0.05, 100,
                self.time_update,
                self._qt_main_ui.axis_c_vel_box
                )
        )

    def init_ui_signals(self):
        self._qt_main_ui.ConnectToOmronBtn.clicked.connect(self.connect)
        self._qt_main_ui.start_btn.clicked.connect(self.start_drivers)
        self._qt_main_ui.stop_btn.clicked.connect(self.stop_drivers)
        self._qt_main_ui.ferq_decriment_btn.clicked.connect(self.dec_ferq)
        self._qt_main_ui.ferq_increment_btn.clicked.connect(self.inc_ferq)

    def create_opc_client(self):
        self.opc_ua_client  = Client(
            self.connect_addres
        )
    def connect(self):
        try:
            self.opc_ua_client.connect()
            self.add_to_log_box("connect to : {}".format(self.connect_addres))
        except Exception as e:
            self.add_to_log_box("connection error : {}".format(str(e)))

    def update(self):
        self.view_update()
        sum_vel = 0
        if self.is_started_drivers:
            self.Time += self.time_update
            for drive in self.Drivers:
                drive.run(self.F)
                sum_vel += round(drive.current_f)
            if sum_vel == 0 and self.is_stop:
                self.is_started_drivers = False
                self.is_stop = False

        pass

    def view_update(self):
        self._qt_main_ui.ferq_lab.display(self.F)
        pass

    def inc_ferq(self):
        if self.F < 50: 
            self.F += 1
    def dec_ferq(self): 
        if self.F > 0:
            self.F -= 1
        


    def start_drivers(self):
        self.Time = 0
        self.is_started_drivers = True
        cmd = self._config_json["hardware_addr"]["start_stop_flag_addr"]
        self.set_value(cmd, self.is_started_drivers)

    def stop_drivers(self):
        self.F = 0
        self.is_stop = True
        cmd = self._config_json["hardware_addr"]["start_stop_flag_addr"]
        self.set_value(cmd, self.is_started_drivers)

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
      