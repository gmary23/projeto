string = 'Geila Maria'

i = 0
# pega o indice 0 e conta a quantidade caracteres 
while i < len(string):
    letra = string[i]

    if letra == ' ':
       break

    print(f'{letra}')
    i += 1
else:
    print('O else foi executado')
print('Esse é o print fora do while.')