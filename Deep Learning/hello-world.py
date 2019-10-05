from sklearn import tree

FEATURES = [[140, 1], [130, 1], [150, 0], [170, 0]]
LABELS = [0, 0, 1, 1]

CLASSIFICADOR = tree.DecisionTreeClassifier()
CLASSIFICADOR = CLASSIFICADOR.fit(FEATURES, LABELS)
FRUTA = CLASSIFICADOR.predict([[150, 0]])
if FRUTA == 1:
    print('\nOrange\n')
else:
    print('\nApple\n')
    