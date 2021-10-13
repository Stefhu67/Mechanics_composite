import numpy as np

class orthotropic():
    def __init__(self, E1, E2, E3, v12, v13, v23, G23, G13, G12):
        self.E1 = E1
        self.E2 = E2
        self.E3 = E3
        self.v12 = v12
        self.v13 = v13
        self.v23 = v23
        self.G12 = G12
        self.G13 = G13
        self.G23 = G23
    def compliance(self):
        S11 = 1/self.E1
        S12 = - self.v12/self.E1
        S13 = -self.v13/self.E1
        S22 = 1/self.E2
        S23 = -self.v23/self.E2
        S33 = 1/self.E3
        S44 = 1/self.G23
        S55 = 1/self.G13
        S66 = 1/self.G12
        return np.array([[S11,S12,S13,0,0,0],[S12,S22,S23, 0, 0, 0], [S13,S23,S33,0,0,0 ], [0,0,0,S44,0,0],[0,0,0,0,S55,0], [0,0,0,0,0,S66]])
    def stiffness(self):
        v21 = self.E2 * self.v12 / self.E1
        v31 = self.E3 * self.v13 / self.E1
        v32 = self.E3 * self.v23 / self.E2
        v = self.v12* v21 + self.v13* v31 + self.v23* v32 + 2* v21*self.v13*v32
        C11 = (1 - self.v23*v32)*self.E1/(1-v)
        C12 = (v21 +v31*self.v23)*self.E1/(1-v)
        C13 = (v31 + v21*v32)*self.E1/(1-v)
        C22 = (1- self.v13 * v31)* self.E2/(1-v)
        C23 = (v32+ self.v12 * v31)*self.E2/(1-v)
        C33 = (1-self.v12*v21)*self.E3/(1-v)
        C44 = self.G23
        C55 = self.G13
        C66 = self.G12
        return np.array([[C11,C12,C13,0,0,0],[C12,C22,C23, 0, 0, 0], [C13,C23,C33,0,0,0 ], [0,0,0,C44,0,0],[0,0,0,0,C55,0], [0,0,0,0,0,C66]])
