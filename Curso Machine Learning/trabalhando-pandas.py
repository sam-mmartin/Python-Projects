'''
import pandas as PD

S = PD.Series([1, 4, 6, 5, 7, 10, 6])

print(S)
print('\n', S[2:4])
print('\n', S.describe())
print('\n', S.mean())
print('\n', S.median())
print('\n', S.duplicated())

S2 = PD.Series([11, 5, 8])
S = S.append(S2)
S.index = PD.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('\n', S)

print()

DF = PD.DataFrame(
    [['fchollet/kera', 11302], ['openai/universe', 4350], ['pandas-dev/pandas', 8168]],
    columns=['Repository', 'Stars']
)
print(DF.shape)
print(DF)
print(DF['Stars'])
print(DF['Stars'].mean())
print(DF['Stars'].median())
print('\nPosicao\n', DF.iloc[1])
print(DF.iloc[1]['Stars'])
print(DF.index)
print('\nIndice\n', DF.ix[0])
DF.index = PD.Index([1, 2, 3])
print(DF)
'''

import pandas as PD
import numpy as NP

#print(help(PD.read_csv))

GATAS = PD.read_csv("Minhas gatas.csv", delimiter=';', encoding='latin-1')
GATAS = GATAS.fillna(0)

#print(GATAS)
#print(GATAS.head())
#print(GATAS.columns)
#print(GATAS['Idade'].describe())
#print(GATAS['Idade'] > 18)
#print(GATAS.loc[GATAS['Idade'] <= 18])

GATAS['Beleza'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
GATAS['Vulgaridade'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')
GATAS['Média'].replace(regex=True, inplace=True, to_replace=r'\D', value=r'')

GATAS['Beleza'] = GATAS['Beleza'].astype(int)
GATAS['Vulgaridade'] = GATAS['Vulgaridade'].astype(int)
GATAS['Média'] = GATAS['Média'].astype(int)

GATAS['Beleza'] = GATAS['Beleza'].astype(float)
GATAS['Vulgaridade'] = GATAS['Vulgaridade'].astype(float)
GATAS['Média'] = GATAS['Média'].astype(float)

GATAS.loc[GATAS.Beleza > 9, 'Beleza'] /= 10
GATAS.loc[GATAS.Vulgaridade > 9, 'Vulgaridade'] /= 10
GATAS.loc[GATAS.Média > 9, 'Média'] /= 10
GATAS['Nota Total'] = GATAS['Sensualidade'] + GATAS['Beleza'] + GATAS['Vulgaridade']

#print('Tamanho - Cidade, Fudi\n', GATAS['Cidade'].nbytes, GATAS['Fudi'].nbytes)

GATAS['Cidade'] = GATAS['Cidade'].astype('category')
GATAS['Fudi'] = GATAS['Fudi'].astype('category')

#print('\nTamanho apos parse - Cidade, Fudi\n', GATAS['Cidade'].nbytes, GATAS['Fudi'].nbytes)

NOME = NP.array(GATAS['Nome'])
BELEZA = NP.array(GATAS['Beleza'])

#print('Nome\n', nome, '\nBeleza\n', beleza)

for i in range(0, len(NOME), 5):
    NOME[i] = NP.nan

for i in range(0, len(BELEZA), 4):
    BELEZA[i] = NP.nan

#print('\nNome\n', nome, '\nBeleza\n', beleza)

DADOS = {
    'Nome': NOME,
    'Beleza': BELEZA
}
DF = PD.DataFrame(DADOS)
#print('\nDataFrame\n', DF)
#print('\nDataFrame - Dropna\n', DF.dropna())
#print('\nDataFrame - Dropna ALL\n', DF.dropna(how='all'))
DF['Serie'] = NP.nan
#print('\nDataFrame - Dropna ALL - Coluna(Eixo Y)\n', DF.dropna(how='all', axis=1))
#print('\nDataFrame - Dropna thresh\n', DF.dropna(thresh=2))
DF['Serie'].fillna(1, inplace=True)
#DF['Beleza'].fillna(DF['Beleza'].mean(), inplace=True)

print(DF[DF['Nome'].notnull() & DF['Beleza'].notnull()])

#print(DF)
