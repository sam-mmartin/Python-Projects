from scipy.spatial import distance

def euclides(A, B):
    return distance.euclidean(A, B)

class KNN_Incompleto():
    def fit(self, X_TRAIN, Y_TRAIN):
        self.X_TRAIN = X_TRAIN
        self.Y_TRAIN = Y_TRAIN
    
    def predict(self, X_TEST):
        PREDICOES = []
        for row in X_TEST:
            label = self.closest(row)
            PREDICOES.append(label)
        return PREDICOES

    def closest(self, row):
        best_dist = euclides(row, self.X_TRAIN[0])
        best_index = 0
        for i in range(1, len(self.X_TRAIN)):
            dist = euclides(row, self.X_TRAIN[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.Y_TRAIN[best_index]

from sklearn import datasets

IRIS = datasets.load_iris()
X = IRIS.data
Y = IRIS.target

from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, Y, test_size=.5)

#from sklearn import tree
#from sklearn.neighbors import KNeighborsClassifier
#CLASSIFICADOR = tree.DecisionTreeClassifier()
#CLASSIFICADOR = KNeighborsClassifier()

CLASSIFICADOR = KNN_Incompleto()
CLASSIFICADOR.fit(X_TRAIN, Y_TRAIN)

PREDICOES = CLASSIFICADOR.predict(X_TEST)
print('\n', PREDICOES)

from sklearn.metrics import accuracy_score
print('\n', accuracy_score(Y_TEST, PREDICOES))