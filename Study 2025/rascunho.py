
class Pessoa:
    
    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    pass


class Cliente(Pessoa):
    pass

p1 = Pessoa('Joao')
a1 = Aluno('Carlos')
c1 = Cliente('Pedro')

print(p1.nome)
print(a1.nome)
print(c1.nome)





