import pandas as PD
from db import DemoDB
'''
DATABASE = DemoDB()

#print(DATABASE.tables)
ALBUM = DATABASE.tables.Album.all()
print(ALBUM.head())

ARTISTA = DATABASE.tables.Artist.all()
print(ARTISTA.head())

#ALBUM_ARTISTA = PD.merge(ARTISTA, ALBUM)
ALBUM_ARTISTA = PD.merge(ARTISTA, ALBUM, on='ArtistId')
print(ALBUM_ARTISTA.head())
'''
alunos1 = PD.DataFrame(
    {
        'nome': ['Alana', 'Rebeca'],
        'nota': [9, 10]
    }
)
alunos2 = PD.DataFrame(
    {
        'nome': ['Dani', 'Aline', 'Bruna'],
        'cod': [1, 2, 3]
    }
)
alunos = PD.merge(alunos1, alunos2, on='nome')
alunos = PD.merge(alunos1, alunos2, how='outer')
print(alunos)
