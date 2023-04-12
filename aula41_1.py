string = 'Geila Maria'

i = 0
# pega o indice 0 e conta a quantidade caracteres 
while i < len(string):
    #cria uma variável e atribui o indice da string
    letra = string[i]
    # aqui fala se encontrar um espaço vazio dentro da string que pare o código
    if letra == ' ':
       break
    #imprime o que tem na variável letra
    print(f'{letra}')
    #o indice passa a ser 1 e volta para início do while e a mágina continua
    i += 1
else:
    print('O else foi executado')
print('Esse é o print fora do while.')