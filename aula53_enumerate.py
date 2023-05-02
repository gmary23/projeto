'''
enmerate - enumera iteráveis (índices)
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')  # acrescenta um item na lista

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
