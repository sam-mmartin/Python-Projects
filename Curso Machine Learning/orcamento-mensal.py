

CABECALHO = ['Descrição', 'Despesas']
DESC_TOTAIS = ['Total Entradas:', 'Total Saidas:', 'TOTAL Restante:']

DESCRICAO = []
ENTRADAS = []
DESPESAS = []
TOTAL = []

X = 0
Y = 0
Z = 0
soma = 0
fechar = ""
POVOARTABELA = ''''''

entry = float(input('Salário do mês: '))
ENTRADAS.append(entry)
print()

while True:
    fechar = input('Descrição da Despesa: ')
    if (fechar == 'x'):
        break
    DESCRICAO.append(fechar)

print()
print('Descrição: ', DESCRICAO)
print()

while True:
    valor = float(input('Valor da Despesa: '))
    if (valor == 0):
        break
    DESPESAS.append(valor)

TOTAL.append(ENTRADAS[0])
TOTAL.append(DESPESAS[0])
TOTAL.append(0)

for i in range(0, len(ENTRADAS)):
    soma += ENTRADAS[i]
    TOTAL[0] = soma

soma = 0

for i in range(0, len(DESPESAS)):
    soma += DESPESAS[i]
    TOTAL[1] = soma

TOTAL[2] = TOTAL[0] - TOTAL[1]
TABELA = [[CABECALHO], [DESCRICAO], [DESPESAS], [ENTRADAS], [DESC_TOTAIS], [TOTAL]]

tamanho = len(DESCRICAO)

for i in range(0, len(TABELA[X][Y])):
    POVOARTABELA += '%s | ' % TABELA[X][Y][i]

X = 1
POVOARTABELA += '\n'

for i in range(0, tamanho):
    POVOARTABELA += '%s | %.2f \n' % (TABELA[X][Y][i],
                                    TABELA[X+1][Y][i])

POVOARTABELA += '\n'
POVOARTABELA += 'TOTAL GERAL'
POVOARTABELA += '\n'

for i in range(0, len(TOTAL)):
    POVOARTABELA += '%s %.2f \n' % (TABELA[4][Y][i], TABELA[5][Y][i])

print()
print(POVOARTABELA)
with open('arquivo.txt', 'w') as file:
    file.write(POVOARTABELA)
