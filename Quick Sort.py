import random

class Quick(object):
    def particao(self, a, inicio, fim):
        randomico = random.randrange(inicio, fim)
        pivo = a[fim-1]
        start = inicio
        end = inicio
        for i in range(inicio, fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1
                start += 1
                aux = a[start-1]
                a[start-1] = a[i]
                a[i] = aux
        return start-1

    def quickSort(self, a, inicio, fim):
        if inicio < fim:
            pp = self.randparticao(a, inicio, fim)
            self.quickSort(a, inicio, pp)
            self.quickSort(a, pp+1, fim)
        return a

    def randparticao(self, a, inicio, fim):
        randomico = random.randrange(inicio, fim)
        aux = a[fim-1]
        a[fim-1] = a[randomico]
        a[randomico] = aux
        return self.particao(a, inicio, fim)

a = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print(a)
q = Quick()
print(q.quickSort(a, 0, len(a)))