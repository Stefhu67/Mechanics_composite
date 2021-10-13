import numpy as np

class orthotropic():
    def __init__(self, E1, E2, v12, G12):
        self.E1 = E1
        self.E2 = E2
        self.v12 = v12
        self.G12 = G12
    def compliance(self):
        S11 = 1/self.E1
        S12 = - self.v12/self.E1
        S22 = 1/self.E2
        S66 = 1/self.G12
        return np.array([[S11,S12,0],[S12,S22, 0],[0,0,S66]])
    def stiffness(self):
        v21 = self.E2 * self.v12 / self.E1
        C11 = self.E1/(1-self.v12*v21)
        C12 = self.v12*self.E2/(1-self.v12*v21)
        C22 = self.E2/(1-self.v12*v21)
        C66 = self.G12
        return np.array([[C11,C12,0],[C12,C22, 0], [0,0,C66]])