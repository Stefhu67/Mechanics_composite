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
                self.E3_o = float(self.orthotropic_material['E3'])
                self.v12_o = float(self.orthotropic_material['v12'])
                self.v13_o = float(self.orthotropic_material['v13'])
                self.v23_o = float(self.orthotropic_material['v23'])
                self.G23_o = float(self.orthotropic_material['G23'])
                self.G13_o = float(self.orthotropic_material['G13'])
                self.G12_o = float(self.orthotropic_material['G12'])

                self.T_isotropic_material = self.doc['T_isotropic_materials']
                self.E1_t = float(self.T_isotropic_material['E1'])
                self.E2_t = float(self.T_isotropic_material['E2'])
                self.v12_t = float(self.T_isotropic_material['v12'])
                self.v23_t = float(self.T_isotropic_material['v23'])
                self.G12_t = float(self.T_isotropic_material['G12'])

                self.isotropic_material = self.doc['Isotropic_materials']
                self.E_i = float(self.isotropic_material['E'])
                self.v_i = float(self.isotropic_material['v'])

                self.stress = self.doc['Stress']
                self.s1 = float(self.stress['s1'])
                self.s2 = float(self.stress['s2'])
                self.s3 = float(self.stress['s3'])
                self.T23 = float(self.stress['T23'])
                self.T13 = float(self.stress['T13'])
                self.T12 = float(self.stress['T12'])

                self.strain = self.doc['Strain']
                self.e1 = float(self.strain['e1'])
                self.e2 = float(self.strain['e2'])
                self.e3 = float(self.strain['e3'])
                self.g23 = float(self.strain['g23'])
                self.g13 = float(self.strain['g13'])
                self.g12 = float(self.strain['g12'])

                self.object = self.doc['Object_dimensions']
                self.L1 = float(self.object['L1'])
                self.L2 = float(self.object['L2'])
                self.L3 = float(self.object['L3'])

                self.temperature = self.doc['Temperature_effect']
                self.alpha1 = float(self.temperature['alpha1'])
                self.alpha2 = float(self.temperature['alpha2'])
                self.alpha3 = float(self.temperature['alpha3'])
                self.D_temp = float(self.temperature['D_temperature'])

                self.humidity = self.doc['Humidity_effect']
                self.beta1 = float(self.humidity['beta1'])
                self.beta2 = float(self.humidity['beta2'])
                self.beta3 = float(self.humidity['beta3'])
                self.D_Moist = float(self.humidity['D_Moisture'])