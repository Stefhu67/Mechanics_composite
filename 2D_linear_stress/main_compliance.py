from Module import *
deck = Deck('./deck.yaml')

Matrix = orthotropic(deck.E1_o, deck.E2_o, deck.v12_o, deck.G12_o)

S_compliance = Matrix.compliance()
print(S_compliance)
stress = np.array([[deck.s1], [deck.s2], [deck.T12]])
strain = np.matmul(S_compliance, stress)
e3 = - deck.v13_o*deck.s1/deck.E1_o - deck.v23_o/deck.E2_o
print(strain)
print(e3)

C_stiffness = Matrix.stiffness()
print(C_stiffness)