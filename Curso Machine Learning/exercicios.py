#===== STRINGS ======
nome = "marcos"

print(nome)
print(type(nome))
print(nome[-1])
print(nome[0])
print(len(nome))
print(nome.__len__())
print(nome[0:3])
print(nome[-3:])
print(nome[-3])

nome = 'Sam'
sobrenome = ' M. Martin'
nome_completo = nome + sobrenome
print(nome_completo)

#======== OPERADORES, REPETIÇÕES ==========
idade = 26
print('%s tem %d anos' % (nome, idade))

#maior = input('Digite sua idade: ')
idade = 26
#print(type(maior))
if idade >= 18:
    if idade >= 60:
        print('Idoso')
    else:
        print('Adulto')
else:
    print('Menor de Idade')

tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print('%d * %d = %d' % (tabuada, numero, tabuada * numero))
        numero += 1
    tabuada += 1

#======== LISTAS ==================
lista = []
print(len(lista))

family1 = ['Samuel', 'Maria', 'Sam', 'Samayhara']
family2 = ['Isabel', 'Silas', 'Maria', 'Jose']
familia = [family1, family2]
print(familia)
x = 0
while x < len(familia):
    y = 0
    while y < len(familia[x]):
        print('\n', familia[x][y], end=' ')
        y += 1
    x += 1
    print('\n')

family = ['Samuel', 'Maria', 'Sam', 'Samayhara']
idades = ['49', '45', '26', '23']
familia = [family, idades]
print(familia)
x = 0
while x == 0:
    y = 0
    while y < len(familia[x]):
        print('\n', familia[x][y], ' = ', familia[x+1][y], end=' ')
        y += 1
    print('\n')
    x = 1

lista = [1, 2, 3, 4]
for e in lista:
    print(e)

busca = 3
for e in lista:
    if e == busca:
        print('Encontrou: ', e)
        break

for i in range(10):
    print(i, end=' ')
print()
for i in range(5, 11):
    print(i, end=' ')
print()
for i in range(2, 11, 2):
    print(i, end=' ')
print()

#====== CONJUNTOS =======
s = set()
type(s)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
uniao = s1.union(s2)
print(uniao)
inter = s1.intersection(s2)
print(inter)
diferenca = s1.difference(s2)
print(diferenca)

#====== DICIONÁRIOS =========
d = {'Sam':26, 'Isabela':20}
print(d)
print(d['Sam'])
d['Aline'] = 29
print(d)
for i in d:
    print(d[i], end=' ')
print()
print(d.items())
print(d.keys())
print(d.values())
print('Maria' in d)
print('Isabela' in d)

print(help(list))