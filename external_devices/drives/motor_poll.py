

import external_devices.drives.RD88 as RD88

class MotorsPoll:
    def __init__(self, config_json, qt_main_ui, controller):
        self.Ferquency           = 20
        self._config_json        = config_json
        self._qt_main_ui         = qt_main_ui
        self.nx_controller       = controller
        self.is_started_drivers  = False
        self.is_stop             = False
        self.min_ferquency_limit = float(config_json["hardware"]["min_limit"])
        self.max_ferquency_limit = float(config_json["hardware"]["max_limit"])
        self.drivers             = []
        self.init_events()
        self.create_group()
        super().__init__()
    
    def init_events(self):
        self._qt_main_ui.ferq_decriment_btn.clicked.connect(self.group_dec_ferq)
        self._qt_main_ui.ferq_increment_btn.clicked.connect(self.group_inc_ferq)
        self._qt_main_ui.start_btn.clicked.connect(self.start_drivers)
        self._qt_main_ui.stop_btn.clicked.connect(self.stop_drivers)

    def create_group(self):
        drv_list = [
            (self.nx_controller,self._config_json["hardware_addr"]["axis_a_set_vel_addr"],self._config_json["hardware_addr"]["axis_a_in_home_flag_addr"],2, 100, self.nx_controller.time_update,self._qt_main_ui.axis_a_vel_box),
            (self.nx_controller,self._config_json["hardware_addr"]["axis_b_set_vel_addr"],self._config_json["hardware_addr"]["axis_b_in_home_flag_addr"],2, 100, self.nx_controller.time_update,self._qt_main_ui.axis_b_vel_box),
            (self.nx_controller,self._config_json["hardware_addr"]["axis_c_set_vel_addr"],self._config_json["hardware_addr"]["axis_c_in_home_flag_addr"],2, 100, self.nx_controller.time_update,self._qt_main_ui.axis_c_vel_box),
            (self.nx_controller,self._config_json["hardware_addr"]["axis_d_set_vel_addr"],self._config_json["hardware_addr"]["axis_d_in_home_flag_addr"],2, 100, self.nx_controller.time_update,self._qt_main_ui.axis_d_vel_box)
        ]

        self.drivers = [ drv for drv in RD88.get_drivers_from_param_list(drv_list) ]



    def update(self):
       self.group_run()

    def group_run(self):
        sum_vel = 0
        if self.is_started_drivers:
            for drive in self.drivers:
                drive.run(self.Ferquency)
                sum_vel += round(drive.current_f)
                print(sum_vel)
            if sum_vel == 0 and self.is_stop:
                self.is_started_drivers = False
                self.is_stop = False

    def group_inc_ferq(self):
        if self.Ferquency > self.max_ferquency_limit:
            self.Ferquency = self.max_ferquency_limit
        else:
            self.Ferquency += 1

    def group_dec_ferq(self):
        if self.Ferquency < self.min_ferquency_limit:
            self.Ferquency = self.min_ferquency_limit
        else:
            self.Ferquency -= 1

    def start_drivers(self):
        self.is_started_drivers = True
        cmd = self._config_json["hardware_addr"]["start_stop_flag_addr"]
        self.nx_controller.set_value(cmd, self.is_started_drivers)

    def stop_drivers(self):
        self.Ferquency = 0
        self.is_stop = True
        cmd = self._config_json["hardware_addr"]["start_stop_flag_addr"]
        self.nx_controller .set_value(cmd, self.is_started_drivers)