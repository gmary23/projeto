"""
Após o 'retorn' nada será executado, veja no exemplo abaixo
"""

def diz_oi():
    return 'oi'
    print('Estou sendo executado após o retorno...')


print(diz_oi())