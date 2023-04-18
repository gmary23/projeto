lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2] # deleta um elemento da lista, conforme o índice indicado
print(lista)
print(lista[2])
lista.append(50) # acrescenta um elemento ao final da lista
lista.pop(40)
print(lista)