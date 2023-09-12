'''
self -> Referencia o que está sendo criado dentro da classe
__init__ -> inicializa os atributos da classes - é uma das primeiras coisas que executada 
'''
class Pessoa: 
    def __init__(self, nome, sobrenome): # o primeiro parametro é sempre reservado para o self - do segundo pode ser usado qualquer um
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Geila', 'Martins')

p2 = Pessoa('Vitor', 'Martins')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)