import numpy as np

class isotropic():
    def __init__(self, E, v):
        self.E = E
        self.v = v
    def compliance(self):
        S11 = 1/self.E
        S12 = - self.v/self.E
        S13 = - self.v/self.E
        S22 = 1/self.E
        S23 = - self.v/self.E
        S33 = 1/self.E
        S44 = 2*(1+self.v)/self.E
        S55 = 2*(1+self.v)/self.E
        S66 = 2*(1+self.v)/self.E
        return np.array([[S11,S12,S13,0,0,0],[S12,S22,S23, 0, 0, 0], [S13,S23,S33,0,0,0 ], [0,0,0,S44,0,0],[0,0,0,0,S55,0], [0,0,0,0,0,S66]])
    def stiffness(self):
        C11 = (1 - self.v)*self.E/((1+self.v)(1-2*self.v))
        C12 = self.v*self.E/((1+self.v)(1-2*self.v))
        C13 = self.v*self.E/((1+self.v)(1-2*self.v))
        C22 = (1 - self.v)*self.E/((1+self.v)(1-2*self.v))
        C23 = self.v*self.E/((1+self.v)(1-2*self.v))
        C33 = (1 - self.v)*self.E/((1+self.v)(1-2*self.v))
        C44 = self.E/(2*(1+self.v))
        C55 = self.E/(2*(1+self.v))
        C66 = self.E/(2*(1+self.v))
        return np.array([[C11,C12,C13,0,0,0],[C12,C22,C23, 0, 0, 0], [C13,C23,C33,0,0,0 ], [0,0,0,C44,0,0],[0,0,0,0,C55,0], [0,0,0,0,0,C66]])