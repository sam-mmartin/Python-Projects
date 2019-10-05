def procura(lista, elemento):
    assert isinstance(lista, list)
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    else:
        return None

lista = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print(lista)
print(procura(lista, 55))
