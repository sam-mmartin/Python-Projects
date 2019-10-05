import matplotlib.pyplot as PLT
import pandas as PD
import mplleaflet
#import numpy as NP

#from pydataset import data
#import seaborn as SNS

'''
X = NP.linspace(1, 10, 100)
print(X)
SNS.set_style('ticks')
IMAGE = PLT.figure()
PLT.plot(X, NP.sin(X), 'r--')
IMAGE.savefig('sin-01.png')
PLT.show()

TITANIC = data()
for i in range(len(TITANIC)):
    print(TITANIC['dataset_id'][i])

TITANIC = data('Traffic')
print(TITANIC.head())
print('\nFrequencia dos anos\n', TITANIC['year'].value_counts())
print('\nAgrupado por Limit\n', TITANIC.groupby('limit')['year'].value_counts())

#TITANIC['y'].value_counts().plot(kind='bar')
TITANIC.groupby('limit')['year'].value_counts().plot(kind='bar')
PLT.show()

UF = PD.read_csv('populacao_brasil.csv')
#Histograma
print(UF.head())
UF['total'].hist()
FIG, EIXO = PLT.subplots()
PLT.hist(UF['total'], bins=15, orientation='horizontal')
EIXO.ticklabel_format(style='plain')

#Gráfico de Pizza
UF['percent'] = UF['total'] / UF['total'].sum()
print(UF.head())
PLT.pie(UF['percent'], labels=UF['estado'], autopct='%1.2f%%')

#Gráfico de Dispersão
DF = data('AirPassengers')
print(DF.head())
#PLT.plot(DF['time'], DF['AirPassengers'])
PLT.scatter(DF['time'], DF['AirPassengers'])

def specie_color(X):
    if X == 'setosa':
        return 0
    elif X == 'versicolor':
        return 1
    return 2

IRIS = data('iris')
IRIS['SpecieNumber'] = IRIS['Species'].apply(specie_color)
print(IRIS.head())
PLT.scatter(
    IRIS['Sepal.Length'], 
    IRIS['Sepal.Width'], 
    sizes=30 * IRIS['Petal.Length'],
    c=IRIS['SpecieNumber'], 
    cmap='viridis', 
    alpha=1
)
'''
IMOVEL = PD.read_csv('copacabana_lat_lng.csv')
PLT.scatter(IMOVEL['lng'], IMOVEL['lat'], marker='.')
mplleaflet.show()
