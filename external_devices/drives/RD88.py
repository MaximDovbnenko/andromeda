
import math

def get_drivers_from_param_list(param):
    for item in param:
        yield Rd88(*item)

class Rd88:
    def __init__(self, controller, set_vel_addr, in_home_addr, k , s, time_interval, view):
        self.omron_nx      = controller
        self.set_vel_addr  = set_vel_addr
        self.in_home_addr  = set_vel_addr
        self.view = view
        self.time_interval = time_interval / 1000
        self.K = k
        self.S = s
        self.t = 0
        self.current_f = 0;
        pass

    def set_vel_from_f(self, f):
        if abs(f) < 0.5 : f = 0.0
        value = round(60 * self.K * self.S * f, 1)
        self.omron_nx.set_value(self.set_vel_addr, value)
        self.view.display(round(f))


    def run(self, f):
        df = round(self.current_f, 1) - round(f, 1)
        direction = 0
        if abs(df) < 0.1 : 
            self.t = 0 
            return
        if df >  0 : direction = -1
        if df <  0 : direction = 1
        self.current_f += self.K *  self.time_interval * direction
        self.t += self.time_interval
        self.set_vel_from_f(self.current_f)
        pass