class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def imprimir_nome(self):
        print(self.nome)
    def imprimir_idade(self):
        print(self.idade)

sam = Pessoa('Sam', 26)
sam.imprimir_nome()
sam.imprimir_idade()

class Conta:
    def __init__(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero

class ContaEspecial(Conta):
    def __init__(self, cliente, numero, limite=0):
        Conta.__init__(self, cliente, numero)
        self.limite = limite

conta = ContaEspecial('Sam', '1234', 100)
print(conta.limite)