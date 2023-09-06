"""
Usando função sem retorno, usando apenas o print 
"""
def quadrado_de_7():
    print(7 * 7)

quadrado_de_7()

"""
Usando função de refatoramento usando o return
"""

def quadrado_de_7():
    return 7 * 7 #

print(quadrado_de_7())

"""
Usando função de refatoramento usando o return
"""

def diz_oi():
    return 'oi'

alguem = ' Pedro!'

print(diz_oi() + alguem)