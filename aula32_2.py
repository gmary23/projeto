"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
entrada = input('Qual seu primeiro nome: ')


nome = len(entrada)
if nome > 0 and nome <= 4:
        print(f'Seu nome tem {nome} caracteres e é curto')
elif nome >= 5 and nome <= 6:
        print('Se nome é normal')
else:
        print('Seu nome é muito grande')
