"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'geila Maria'
outra_string = f'{string[:5]}ABC{string[8:]}'

# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
print(outra_string)

#print(string.zfill(50)) #preenche espaços vazios.
#print(string.capitalize()) #Trasforma a primeira letra em maiúscula.