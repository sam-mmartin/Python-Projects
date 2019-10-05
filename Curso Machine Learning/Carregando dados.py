import numpy as np

valor1, valor2, valor3 = np.loadtxt('dados.txt', skiprows=1, unpack=True)
print(valor1)
print(valor2)
print(valor3)

matriz = np.genfromtxt('dadosFaltantes.txt', skip_header=1, filling_values=0)
print(matriz)