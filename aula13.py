nome = 'Geila'
altura = 1.60
peso = 63
imc = peso / (altura ** 2)

#Formatação de string, coloca-se um "f" antes do início usa-se chave
#verificar exemplo abaixo
linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.5f}'

print (linha_1)
print (linha_2)

'''
print(nome, 'tem', altura, 'de altura')
print("pesa", peso,'quilos e seu IMC é')
print(imc)
'''

