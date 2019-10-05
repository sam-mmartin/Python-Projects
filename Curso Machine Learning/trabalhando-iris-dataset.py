import numpy as NP
from sklearn.datasets import load_iris

IRIS = load_iris()

DADOS = IRIS.data
print(DADOS[:50, 0])

import matplotlib.pyplot as PLT

PLT.plot(DADOS[:50, 0], c='Red', ls=':', marker='s', ms='5', label='Comp. Sépala Setosa')
PLT.plot(DADOS[50:100, 0], c='Blue', ls=':', marker='s', ms='5', label='Comp. Sépala Versicolor')
PLT.plot(DADOS[100:150, 0], c='Yellow', ls=':', marker='o', ms='5', label='Comp. Sépala Virginica')

PLT.show()