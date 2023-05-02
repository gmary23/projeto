'''
Operação ternária - basicamente é o 'if' e 'else' na mesma linha

'''
digito = 12  # 9 = 0
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
