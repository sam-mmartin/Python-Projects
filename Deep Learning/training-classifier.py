SCORES = [3.0, 1.0, 0.2]

import numpy as NP

def softmax(x):
    """Compute softmax values for x."""
    return NP.exp(x) / NP.sum(NP.exp(x), axis=0)

print(softmax(SCORES))

import matplotlib.pyplot as PLT

X = NP.arange(-2.0, 6.0, 0.1)
SCORES = NP.vstack([X, NP.ones_like(X), 0.2 * NP.ones_like(X)])

PLT.plot(X, softmax(SCORES).T, linewidth=2)
PLT.show()