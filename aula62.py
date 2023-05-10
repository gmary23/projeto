"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
cpf_enviado_usuario = "74682489070"
nove_digitos = cpf_enviado_usuario[:9]  # os 9 primeiros dígitos
contador_regressivo_1 = 10

resultado_digito_1 = 0  # variável vazia
for digito in nove_digitos:  # para cada dígito dos dígitos que existem
    # multiplica os dígitos que informei com o contador regressivo e soma todos
    resultado_digito_1 += int(digito) * contador_regressivo_1
    # esse comando faz com que comece do 10 e conte de traz pra frente
    # conta o outro número, sendo que começa do maior para o menor
    contador_regressivo_1 -= 1
# pega o resultado...multiplica por 10
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_dgitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f"{nove_digitos}{digito_1}{digito_2}"

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f" {cpf_enviado_usuario} é valido")
else:
    print("CPF inválido")
