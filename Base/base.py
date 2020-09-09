

class SystemState:
    def __init__(self, opc_server):
        self.current_ferquency = 0

        self.a_b_error         = 0
        self.a_c_error         = 0
        self.a_d_error         = 0
        
        self.a_position        = 0
        self.b_position        = 0
        self.c_position        = 0
        self.d_position        = 0

        self.opc_server_obj    = opc_server

        pass

    def getPositions(self):
        if self.opc_server_obj.conected
        pass
    def update(self):
        pass