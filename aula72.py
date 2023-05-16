# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


# def multiplicar(*args): # criada a função multiplicar que empacota todos os números que for enviados
#    total = 1 # começa do 1, pq se iniciar do 0...vai sempre multiplicar pelo 0 e ñ dá outro número
#    for numero in args:  #pega todos os numeros que tem em args
#        total *= numero # multiplica o total pelo o numero que existir
#    return total # retorna o total


# multiplicacao = multiplicar(1, 1, 2)  # cria uma variável chamada multiplicação e colocar o valores da função
# print(multiplicacao)  # imprime a variável


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(numero):  # uma função com o valor número
    return numero % 2 == 0  # verifica se dividido por 2 não retorna nada


print(par_impar(1))  # retorna False
print(par_impar(2))  # retorna True
print(par_impar(5))  # retorna False
print(par_impar(8))  # retorna True
