'''
Criando uma função que joga moeda
'''
from random import random

def joga_moeda():
    valor = random() # gera número pseudo-randômico entre 0 e 1
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())