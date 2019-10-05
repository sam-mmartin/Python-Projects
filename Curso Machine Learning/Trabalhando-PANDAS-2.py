import pandas as PD
import numpy as NP

DF = PD.read_csv('primary-results.csv')

#print(DF.head())
#print(len(DF))
#print(DF.groupby('candidate'))
'''print(
    DF.groupby('candidate').aggregate(
        {
            'votes': [min, NP.mean, max]
        }
    )
)'''
#print(DF[DF['votes'] == 590502])
'''print(
    DF.groupby('candidate').aggregate(
        {
            'fraction_votes': [min, NP.mean, max]
        }
    )
)'''
#print(DF[DF['fraction_votes'] == 1])
'''print(
    DF[
        (DF['fraction_votes'] == 1) & (DF['candidate'] == 'Hillary Clinton')
    ]
)
def fracao_votos_filtro(X):
    return X['votes'].sum() > 1000000

#print(DF.groupby('state').filter(fracao_votos_filtro))
#print(DF[DF['state_abbreviation'] == 'AL']['votes'].sum())
print(DF.groupby(['state_abbreviation', 'candidate'])['votes'].sum())
'''
print('Candidatos\n')
for i in range(len(DF['candidate'].unique())):
    print(DF['candidate'].unique()[i])

print('\nPivot Table Votos\n', PD.pivot_table(
    DF, index=['state', 'party', 'candidate'], values=['votes'],
    aggfunc={'votes': NP.sum}
))

DF['rank'] = DF.groupby(['county', 'party'])['votes'].rank(ascending=False)
print('\nVotos por Distrito\n', DF[DF['county'] == 'Los Angeles'])

DF_GROUPBY = DF.groupby(['state', 'party', 'candidate']).sum()
del DF_GROUPBY['fips']
del DF_GROUPBY['fraction_votes']
DF_GROUPBY.reset_index(inplace=True)
print('\nAgrupado por Estado, Partido e Candidato\n', DF_GROUPBY.head())

DF_GROUPBY['rank'] = DF_GROUPBY.groupby(['state', 'party'])['votes'].rank(ascending=False)
print('\nAgrupado pelo Rank de Votos\n', DF_GROUPBY.head(10))

print(
    '\nPivot Table Votos por Estado, partido e candidatos\n',
    PD.pivot_table(
        DF_GROUPBY, index=['state', 'party', 'candidate'], values=['rank', 'votes']
    )
)

print(
    '\nRanking dos Candidatos\n',
    DF_GROUPBY[DF_GROUPBY['rank'] == 1]['candidate'].value_counts()
)