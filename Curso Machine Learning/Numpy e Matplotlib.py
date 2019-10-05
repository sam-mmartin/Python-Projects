import numpy as np
import matplotlib.pyplot as plt

SALARIO = np.array([1100, 1000, 1100, 1100, 1500])
print('Salario: ', SALARIO)
#plt.plot(SALARIO, c='Red', ls='--', marker='s', label='Salarios')
#plt.legend(loc='upper left')
#plt.show()

VETOR = np.array([1, 2, 3])
print('\nVetor\n', VETOR)
print(np.insert(VETOR, 1, 10))
MATRIX = np.array([[10, 20], [30, 40]])
print('\nMatrix\n', MATRIX)
print('\nSoma eixo 1', MATRIX.sum(axis=0))
print('Soma eixo 2', MATRIX.sum(axis=1))
print('Inserir eixo 1\n', np.insert(MATRIX, 2, 30, axis=0))
print('Inserir eixo 2\n', np.insert(MATRIX, 2, 30, axis=1))
print('\nAdiciona ao final\n', np.append(MATRIX, [[50, 60]], axis=0))

A = np.array([[1, 2], [3, 4], [5, 6]])
print('\nA\n', A)
print('\nDeleta no eixo X\n', np.delete(A, 1, 0))
print('\nDeleta no eixo Y\n', np.delete(A, 0, 1))

B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print('\nB\n', B)
print('\nDeleta de 2 em 2\n', np.delete(B, np.s_[::2], 0))

C = np.array([[1, 2], [3, 4]])
print('\nC\n', C)
print('\nRepete 2x\n', np.repeat(C, 2))
print('\nRepete 3x\n', np.repeat(C, 3))
print('\nRepete 2x no eixo X\n', np.repeat(C, 2, axis=1))

D = np.array([[1, 2, 3]])
print('\nD\n', D)
print('\nRepete o array 2x\n', np.tile(D, 2))
print('\nRepete o array 3x\n', np.tile(D, 3))

print('\nRepete o array 2x\n', np.tile(C, 2))

E = np.array([[1, 2, 3], [4, 5, 6]])
print('\nE\n', E)
print('\nDivide o array em 2 no eixo X\n', np.array_split(E, 2, axis=0))
print('\nDivide o array em 2 no eixo Y\n', np.array_split(E, 2, axis=1))

print('\nDivide o array em 2 no eixo Y\n', np.array_split(B, 2, axis=0))

print('\n Array de 0s\n', np.zeros(4))
print('\n Array de 0s\n', np.zeros((5, 5)))
print('\nArray de 1s\n', np.ones((10, 10)))

print('\nMatriz Identidade\n', np.eye(10))

print('\nMaiores que 3 na matriz A\n', A[A > 3])
print('\nMaiores que 1 na matriz A\n', A[A > 1])
IDX = (A > 2)
print('\nIndexacao na matriz A\n', IDX)

print('\nConcatenar Arrays D e E no eixo Y\n', np.concatenate((D, E), axis=0))
print('\nConcantenar Arrays C e E no eixo X\n', np.concatenate((C, E), axis=1))

F = np.arange(10)
print('\nSequencia\n', F)
np.random.shuffle(F)
print('\nSequencia Shuffle\n', F)

print('\nSequencia Uniformemente Espacada\n', np.linspace(1, 10, 5))
print('\nElementos unicos de um Array\n', np.unique(D))
