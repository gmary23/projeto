'''
Calculando o segundo dígito
'''

cpf = '64143473372'
dez_digitos = cpf[:10]  # os 10 primeiros dígitos
contador_regressivo = 11

resultado_digito_2 = 0  # variável vazia
for digito_2 in dez_digitos:  # para cada dígito dos dígitos que existem
    # multiplica os dígitos que informei com o contador regressivo e soma todos
    resultado_digito_2 += int(digito_2) * contador_regressivo
    # esse comando faz com que comece do 10 e conte de traz pra frente
    contador_regressivo -= 1  # conta o outro número, sendo que começa do maior para o menor
# pega o resultado...multiplica por 10
digito_2 = (resultado_digito_2 * 10 % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)
