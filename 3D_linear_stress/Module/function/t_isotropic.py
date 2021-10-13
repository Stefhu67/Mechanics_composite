import numpy as np

class t_isotropic():
    def __init__(self, E1, E2, v12, v23, G12):
        self.E1 = E1
        self.E2 = E2
        self.v12 = v12
        self.v23 = v23
        self.G12 = G12
    def compliance(self):
        E3 = self.E2
        v13 = self.v12
        G13 = self.G12
        G23 = self.E2/(2*(1+self.v23))
        S11 = 1/self.E1
        S12 = - self.v12/self.E1
        S13 = - v13/self.E1
        S22 = 1/self.E2
        S23 = -self.v23/self.E2
        S33 = 1/E3
        S44 = 1/G23
        S55 = 1/G13
        S66 = 1/self.G12
        return np.array([[S11,S12,S13,0,0,0],[S12,S22,S23, 0, 0, 0], [S13,S23,S33,0,0,0 ], [0,0,0,S44,0,0],[0,0,0,0,S55,0], [0,0,0,0,0,S66]])
    def stiffness(self):
        E3 = self.E2
        v13 = self.v12
        G13 = self.G12
        G23 = self.E2/(2*(1+self.v23))
        v21 = self.E2 * self.v12 / self.E1
        v31 = E3 * v13 / self.E1
        v32 = E3 * self.v23 / self.E2
        v = self.v12* v21 + v13* v31 + self.v23* v32 + 2* v21*v13*v32
        C11 = (1 - self.v23*v32)*self.E1/(1-v)
        C12 = (v21 +v31*self.v23)*self.E1/(1-v)
        C13 = (v31 + v21*v32)*self.E1/(1-v)
        C22 = (1- v13 * v31)* self.E2/(1-v)
        C23 = (v32+ self.v12 * v31)*self.E2/(1-v)
        C33 = (1-self.v12*v21)*E3/(1-v)
        C44 = G23
        C55 = G13
        C66 = self.G12
        return np.array([[C11,C12,C13,0,0,0],[C12,C22,C23, 0, 0, 0], [C13,C23,C33,0,0,0 ], [0,0,0,C44,0,0],[0,0,0,0,C55,0], [0,0,0,0,0,C66]])