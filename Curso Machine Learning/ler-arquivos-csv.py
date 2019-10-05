import numpy as NP

raking, nome, idade, cidade, fudi, sensualidade, beleza, vulgaridade, media = NP.genfromtxt("Minhas gatas.csv", delimiter=";", skip_header=1, unpack=True)
print('\nRaking\n', raking)
print('\nNome\n', nome)
print('\nIdade\n', idade)
print('\nCidade\n', cidade)
print('\nFudi ela\n', fudi)
print('\nSensualidade\n', sensualidade)
print('\nBeleza\n', beleza)
print('\nVulgaridade\n', vulgaridade)
print('\nMedia\n', media)


import csv
lista = []

with open("Minhas gatas.csv", newline='') as csvfile:
    conteudo = csv.reader(csvfile, delimiter=';')
    for linha in conteudo:
        lista.append(linha)

descricao = lista[0]
ranking = []
nome = [] 
idade = [] 
cidade = []
fudi= []
sensualidade = [] 
beleza = []
vulgaridade = []
media = []
for i in range(1, len(lista)):
    ranking.append(lista[i][0])
    nome.append(lista[i][1])
    idade.append(lista[i][2])
    cidade.append(lista[i][3])
    fudi.append(lista[i][4])
    sensualidade.append(lista[i][5])
    beleza.append(lista[i][6])
    vulgaridade.append(lista[i][7])
    media.append(lista[i][8])

tabela2 = [[descricao], [ranking], [nome], [idade], [cidade], [fudi], [sensualidade], [beleza], [vulgaridade], [media]]

tamanho = len(ranking)
X = 0
Y = 0
Z = 0
POVOARTABELA = ''''''

for i in range(0, len(tabela2[X][Y])):
    POVOARTABELA += '%s | ' % tabela2[X][Y][i]
X = 1
POVOARTABELA += '\n'
for i in range(0, tamanho):
    POVOARTABELA += '| %s | %s | %s | %s | %s | %s | %s | %s | %s \n' % (tabela2[X][Y][i], 
    tabela2[X+1][Y][i], 
    tabela2[X+2][Y][i],
    tabela2[X+3][Y][i],
    tabela2[X+4][Y][i],
    tabela2[X+5][Y][i],
    tabela2[X+6][Y][i],
    tabela2[X+7][Y][i],
    tabela2[X+8][Y][i])

print(POVOARTABELA)
with open('gatas.txt', 'w') as file:
    file.write(POVOARTABELA)
