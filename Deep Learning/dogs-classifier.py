import numpy as NP
import matplotlib.pyplot as PLT

GALGO_INGLES = 500
LABRADOR = 500

GALGO_HEIGHT = 28 + 4 * NP.random.randn(GALGO_INGLES)
LABRADOR_HEIGHT = 24 + 4 * NP.random.randn(LABRADOR)

PLT.hist([GALGO_HEIGHT, LABRADOR_HEIGHT], stacked=True, color=['r', 'b'])
PLT.show()
