# Mais exemplo de "in"
nome = input('Digite seu nome: ')
encontrar = input('Digite o que vc deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')