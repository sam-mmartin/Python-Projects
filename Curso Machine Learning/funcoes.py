dobro = lambda x: x * 2
print(dobro(3))
soma = lambda x, y: x + y
print(soma(10, 20))
lista = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, lista)))
print(list(map(lambda x: x * 2, lista)))

