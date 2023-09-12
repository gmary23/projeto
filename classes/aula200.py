'''
Métodos em instâncias de classes Python

self é o mesmo que o objeto fora da classe
o método init SEMPRE retorna NONE
Hard coded -> algo que foi escrito diretamente no código

Um método é uma função que está dentro da classe - e usa o primeiro parametro tem de ser
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...') # print dentro do método

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(fusca.nome)
celta.acelerar()