
import random

class SimulationOmron:
    def __init__(self):
        self.PositionA = 0
        self.PositionB = 0
        self.PositionC = 0
        self.PositionD = 0
        self.Threshold = 10
        self.va = 0.1
        self.vb = 0.1
        self.vc = 0.1
        self.vd = 0.1
    def SetVelByAxis(self, axis, vel):
        if(axis == 'a' or axis == 'A'):
            self.va = vel
        elif(axis == 'b' or axis == 'B'):
            self.vb = vel
        elif(axis == 'c' or axis == 'C'):
            self.vc = vel
        elif(axis == 'd' or axis == 'D'):
            self.vd = vel
        else:
            print('Axis ' + str(axis) + " not exist!")
    def Update(self):
        rnd_A = random.random() * 100
        if rnd_A > self.Threshold:
            self.PositionA = self.PositionA + 1

        rnd_B = random.random() * 100
        if rnd_B > self.Threshold:
            self.PositionB = self.PositionB + 1

        rnd_C = random.random() * 100
        if rnd_C > self.Threshold:
            self.PositionC = self.PositionC + 1
        
        rnd_D = random.random() * 100
        if rnd_D > self.Threshold:
            self.PositionD = self.PositionD + 1