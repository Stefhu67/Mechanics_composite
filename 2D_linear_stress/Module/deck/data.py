import yaml, sys
import numpy as np
import os.path

class Deck():
    def __init__(self, inputhpath):
        if not os.path.exists(inputhpath):
            print("File " + inputhpath)
            sys.exit(1)
        else:
            with open(inputhpath,'r') as f:
                ## Container of the tags parsed from the yaml file
                self.doc = yaml.load(f, Loader=yaml.BaseLoader)
                self.orthotropic_material = self.doc['Orthotropic_materials']
                self.E1_o = float(self.orthotropic_material['E1'])
                self.E2_o = float(self.orthotropic_material['E2'])
                self.v12_o = float(self.orthotropic_material['v12'])
                self.v13_o = float(self.orthotropic_material['v13'])
                self.v23_o = float(self.orthotropic_material['v23'])
                self.G12_o = float(self.orthotropic_material['G12'])

                self.stress = self.doc['Stress']
                self.s1 = float(self.stress['s1'])
                self.s2 = float(self.stress['s2'])
                self.T12 = float(self.stress['T12'])

                self.strain = self.doc['Strain']
                self.e1 = float(self.strain['e1'])
                self.e2 = float(self.strain['e2'])
                self.e3 = float(self.strain['e3'])
                self.g23 = float(self.strain['g23'])
                self.g13 = float(self.strain['g13'])
                self.g12 = float(self.strain['g12'])