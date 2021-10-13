from Module import *
deck = Deck('./deck.yaml')

#Matrix = orthotropic(deck.E1_o, deck.E2_o, deck.E3_o, deck.v12_o, deck.v13_o, deck.v23_o, deck.G23_o, deck.G13_o, deck.G12_o)

#Matrix = t_isotropic(deck.E1_t, deck.E2_t, deck.v12_t, deck.v23_t, deck.G12_t)

Matrix = isotropic(deck.E_i, deck.v_i)

S_compliance = Matrix.compliance()
print(S_compliance)
stress = np.array([[deck.s1], [deck.s2], [deck.s3], [deck.T23], [deck.T13], [deck.T12]])
strain_tot = np.matmul(S_compliance, stress)
strain_mech = strain_tot + np.array([[- deck.alpha1 * deck.D_temp -deck.beta1 * deck.D_Moist],[- deck.alpha2 * deck.D_temp - deck.beta2 * deck.D_Moist],[- deck.alpha3 * deck.D_temp - -deck.beta3 * deck.D_Moist],[0],[0],[0]])
print(strain_tot)
cube = np.array([[deck.L1], [deck.L2], [deck.L3], [0], [0], [0]])
delta_l = cube *strain_mech
print(delta_l)