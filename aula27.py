"""
FATIAMENTO DE STRINGS
 012345678 -> INDICE POSITIVO
 Olá mundo
-987654321 -> INDICE NEGATIVO
Fatiamento [i:f:p] aqui se refere ao início e fim e um passo [::]
Obs.: a função len retorna a qtd de caracteres da str

"""
# Checa o tamanho de uma string/objeto.
variavel = 'Olá mundo'
print(len(variavel)) #aqui não se refere a indice, mas sim a quantidades de caracteres da strings


variavel = 'Olá mundo'
print(variavel[::-1]) # ele conta do inicio ao fim, mas conta os de traz pra frente

variavel = 'Olá mundo'
print(variavel[::1]) # aqui ele diz pra começar do inicio e ir até o fim e passar por todas as casas

variavel = 'Olá mundo'
print(variavel[::2]) #aqui vai do inicio ao fim, mas pulando duas casas.

ariavel = 'Olá mundo'
print(variavel[0:5]) #aqui vai do 0 até o 5.