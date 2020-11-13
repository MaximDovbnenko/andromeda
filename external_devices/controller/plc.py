
import external_devices.controller.arduino as relay
import time
class PLC:
    def __init__(self, config_json, qt_main_ui, controller):
        self._qt_main_ui   = qt_main_ui
        self.nx_controller = controller
        self.io_contriller = relay.ArduinoRelay(config_json)
        self.alarm_delay = 10
        self.alarm_count = 0
        self.is_alarm    = False
        self.init_events()
        super().__init__()

    def init_events(self):
        self._qt_main_ui.power_enable_btn.clicked.connect(self._set_enable_ac)
        self._qt_main_ui.power_disable_btn.clicked.connect(self._set_disable_ac)
        self._qt_main_ui.clear_error_btn.clicked.connect(self._set_alarm_off)

    def alarm(self):
        if self.alarm_count > self.alarm_delay:
            self.io_contriller.alarm()
            self.alarm_count  = 0
        else:
            self.alarm_count += 1

    def update(self):
        if self.is_alarm: self.alarm()
        pass


    def _set_alarm_on(self, delay = 10):
        self.alarm_delay = delay
        self.alarm_count = 0
        self.is_alarm    = True

    def _set_alarm_off(self):
        self.is_alarm    = False
        self.io_contriller.send(self.io_contriller.ALARM_OFF_CMD)

    def _set_enable_ac(self):
        if not self.is_alarm:
            if  self.nx_controller.is_opcua_connected:
                self.io_contriller.motors_enable()
                time.sleep(0.5)
                self.io_contriller.turn_on_ac()
            else:
                self.is_alarm = True
                
    def _set_disable_ac(self):
        self.io_contriller.motors_disable()
        time.sleep(0.5)
        self.io_contriller.turn_off_ac()
       