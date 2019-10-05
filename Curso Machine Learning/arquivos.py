"""file = open('arquivo.txt', 'w')
file.write('Machine Learning')
texto = '''
Aprendendo Python
machine learning
python e foda
'''
file.write(texto)
file.close()"""

"""lista = ['Sam', 'Isabela', 'Aline', 'Alana', 'Larissa', 'Mary']
idade = [26, 20, 29, 25, 16, 29]
casal = [lista, idade]
x = 0
y = 0
texto = ''''''
while x == 0:
    while y < len(casal[x]):
        texto += '%s %d \n' % (casal[x][y], casal[x+1][y])
        y += 1
    x = 1

with open('arquivo.txt', 'w') as file:
    file.write(texto)"""

CABECALHO = ['Valores 1', 'Valores 2', 'Valores 3']
VALORES = [0.1212, 0.842, 0.3672,
           0.104, 0.5422, 0.34551,
           0.5661, 0.932, 0.2332,
           0.762, 0.847361, 0.1538]
X = 0
Y = 0
Z = 0
POVOARTABELA = ''''''
while X == 0:
    while Y < len(CABECALHO):
        POVOARTABELA += '%s\t' % CABECALHO[Y]
        Y += 1
    POVOARTABELA += '\n'
    while Z < len(VALORES):
        POVOARTABELA += '%f\t' % VALORES[Z]
        if (Z+1) % 3 == 0:
            POVOARTABELA += '\n'
        Z += 1
    X = 1

with open('dados.txt', 'w') as file:
    file.write(POVOARTABELA)

with open('dados.txt', 'r') as file:
    #print(file.readlines())
    #for linha in file.readlines():
       #print(linha)
    CONTEUDO = file.read()
    print(CONTEUDO)
    #lista = file.read().splitlines()
    #print(lista[0])
    #print(len(lista))
    