import numpy as np

A = np.array([10, 20, 30, 40])
print('Tipo do dado: ', type(A))
print('Array\n', A)

MAT = np.array([[1, 2], [3, 4]])
print('Matriz\n', MAT)
print('Ultimo elemento da matriz\n', MAT[1][1])
print('Ultimo elemento da matriz\n', MAT[-1][-1])
print('Linha\n', MAT[1, :])
print('Coluna\n', MAT[:, 0])
print('Matriz transposta\n', MAT.transpose())

M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])
print('Soma de Matrizes\n', M1 + M2)
print('Subtracao de matrizes\n', M1 - M2)
print('Produto de matrizes\n', M1 * M2)
print('Maior indice da matriz: ', M1.argmax())
print('Menor indice da matriz: ', M2.argmin())

print('Media: ', A.mean())
print('Diagonal: ', MAT.diagonal())
print('Dimensao a: ', A.ndim, 'Dimensao mat: ', MAT.ndim)

SOMA = 0
#for i in range(1, 100000001):
#    soma += i
print(np.arange(1, 100000001).sum())

L = [20, 40, 60, 80]
print('Lista\n', L)
print(L[1:3])
print(L[::2])

LISTA = np.array(L)
print('Array\n', LISTA)
print(LISTA[1:3])
print(LISTA[::2])

L2 = L[:]
print('Lista 2\n', L2)
L2[0] = 1000
print(L2)

L3 = L.copy()
print(L)
print(L2)
print(L3)

ALANA = [8, 9, 8, 10]
ALINE = [7, 8, 7, 9]
THAY = [9, 8, 8, 8]
REBECA = [10, 8, 9, 10]

GATAS = np.array([ALANA, ALINE, THAY, REBECA])
print('\nGatas\n', GATAS)
print()
print(GATAS[0])
print(GATAS[1][0])

ALEA = np.arange(0, 20)
print(ALEA)

MATR = np.reshape(ALEA, (5, 4))
print('Matrix\n', MATR)
print(MATR.item(5))
MATRIX1 = np.array([[1, 2, 3], [4, 5, 6]])
MATRIX2 = np.array([[10, 20, 30], [40, 50, 60]])
print('\nMATRIX\n', MATRIX1, '\n\n', MATRIX2)
print('Divisao\n', MATRIX2 / MATRIX1, '\n\n', MATRIX1 / MATRIX2)
print(np.matrix.round(MATRIX1 / MATRIX2))
print('\nx 10\n', 10 * MATRIX1)
print('\n+ 5\n', MATRIX1 + 10)
print('\n- 1\n', MATRIX1 - 1)
print('\nMultiplicacao\n', MATRIX1 * MATRIX2)
print('\nPonteciacao\n', MATRIX1 ** 2, '\n\n', MATRIX2 ** 2)