import numpy as NP
from sklearn.datasets import load_iris
from sklearn import tree

IRIS = load_iris()
'''
print(IRIS.feature_names)
print(IRIS.target_names)
print(IRIS.data[0])
print(IRIS.target_names[0])

for i in range(len(IRIS.target)):
    print('\nExample %d: label %s, feature %s' % (i, IRIS.target[i], IRIS.data[i]))
'''

TESTE_IDX = [0, 50, 100]
# training data
TRAIN_TARGET = NP.delete(IRIS.target, TESTE_IDX)
TRAIN_DATA = NP.delete(IRIS.data, TESTE_IDX, axis=0)
# testing data
TEST_TARGET = IRIS.target[TESTE_IDX]
TESTE_DATA = IRIS.data[TESTE_IDX]

CLASSIFICADOR = tree.DecisionTreeClassifier()
CLASSIFICADOR.fit(TRAIN_DATA, TRAIN_TARGET)

print(TEST_TARGET)
print('\n', CLASSIFICADOR.predict(TESTE_DATA))
