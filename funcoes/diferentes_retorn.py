'''
Em uma função tem diferentes retorn - no exemplo abaixo mostra isso dentro 
'''

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

'''
Aqui o retorno será 3.2, pq a variável foi declarada None, e nessa condição retorna esse valor
'''
def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

'''
Aqui o retorno será b, pq a variável foi declarada False, devido a última condição
'''
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())