from Module import *
deck = Deck('./deck.yaml')

#Matrix = orthotropic(deck.E1_o, deck.E2_o, deck.E3_o, deck.v12_o, deck.v13_o, deck.v23_o, deck.G23_o, deck.G13_o, deck.G12_o)

Matrix = t_isotropic(deck.E1_t, deck.E2_t, deck.v12_t, deck.v23_t, deck.G12_t)

C_stiffness = Matrix.stiffness()
print(C_stiffness)
strain = np.array([[deck.e1], [deck.e2], [deck.e3], [deck.g23], [deck.g13], [deck.g12]])
stress = np.matmul(C_stiffness, strain)
print(stress)