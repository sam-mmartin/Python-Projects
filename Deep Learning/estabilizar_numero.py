X = 1000000000
Y = 0.000001

for i in range(1, 1000000):
    X += Y
print(X)
X = X - 1000000000
print(X)

for i in range(1000000):
    Y += Y
print(Y)