import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)
class ArduinoRelay:
    def __init__(self, config):
        self.port  = config["hardware"]["arduino_port"]
        self.bound = config["hardware"]["arduino_bound"]
        self.TURN_ON_CMD       = bytearray([100,1,1,0,0,0,0,0,0,0])
        self.TURN_OFF_CMD      = bytearray([100,1,0,0,0,0,0,0,0,0])
        self.ALARM_ON_CMD      = bytearray([100,2,1,0,0,0,0,0,0,0])
        self.ALARM_OFF_CMD     = bytearray([100,2,0,0,0,0,0,0,0,0])
        self.MOTOR_ENABLE_CMD  = bytearray([100,3,1,0,0,0,0,0,0,0])
        self.MOTOR_DISABLE_CMD = bytearray([100,3,0,0,0,0,0,0,0,0])

        self.alarm_flag   = False
        try:
            self.serial_port = serial.Serial(self.port, self.bound )
        except Exception as e:
            pass

    
    def alarm(self):
        if not self.alarm_flag:
            self.send(self.ALARM_ON_CMD)
            self.alarm_flag = True
        else:
            self.alarm_flag = False
            self.send(self.ALARM_OFF_CMD)

    def turn_on_ac(self):
        self.send(self.TURN_ON_CMD)
     

    def turn_off_ac(self):
        self.send(self.TURN_OFF_CMD)

    def motors_enable(self):
        self.send(self.MOTOR_ENABLE_CMD)

    def motors_disable(self):
        self.send(self.MOTOR_DISABLE_CMD)

    def send(self, data):
        try:
            self.serial_port.write(data)
        except Exception as e:
            pass
