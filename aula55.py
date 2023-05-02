# a terceira opção (decimal) para trabalhar imprecisão em pontos flutuantes.
import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
# a primeira opção(f'string) as duas casas decimais após o ponto.
print(f'{numero_3:.2f}')
# a segunda opçao (a função round) que arredonda na quantidade que desejar
print(round(numero_3, 2))
