'''
Entendendo self em classes Python
Classe - Molde (geralmente sem dados)
Instancia da class (objeto) - tem dados
Uma classe pode gerar várias instâncias
Na classe o self é a própria instância
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...') # print dentro do método

fusca = Carro('Fusca')
fusca.acelerar() # aqui é o molde (exemplificado como uma forma para biscoito na aula)
#Carro.acelerar(fusca)

celta = Carro('Celta')
celta.acelerar()

