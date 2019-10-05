def searchB(lista, elemento):
    inicio = 0
    fim = len(lista)-1
    meio = (len(lista))  
    
    while inicio <= fim:
        if meio % 2 == 0:
            meio = meio / 2
            meio = int(meio)
        else:
            meio = (meio - 1) / 2
            meio = int(meio)
        if elemento == lista[meio]:
            return meio
        if elemento < lista[meio]:
            fim = meio - 1
            meio = fim
        else:
            inicio = meio + 1
    
    return -1

lista = [8,5,12,55,3,7,82,44,35,25]
print(searchB(lista, 5))