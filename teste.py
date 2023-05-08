'''
qdade_linha = 5
qtade_coluna = 5

linha = 1
while linha <= qdade_linha:
    

    coluna = 1
    while coluna <= qtade_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

nome = 'Geila'

novo_nome = ''
contador = 0
while contador < len(nome):
      letra = nome[contador] # crei uma nova variável com o nome "letra" e coloquei o nome com o índice dentro
      novo_nome += f'*{letra}' # a variável "novo_nome" que era vazia agora recebeu as informações que tem na variável "letra" ou seja (o nome com o índice).
      contador += 1 # soma com mais 1 e volta ao início do while
      
    

print(novo_nome)


nome = 'Geila'

indice = 0
new_name = ''
while indice < len(nome):
    letra = nome[indice] # recebe as informações do nome com os índices, isso faz ficar um abaixo do outro
    new_name += f'*{letra}'# aqui a nova variável "new_name" recebe o que tem dentro de "letra"
    indice += 1

print(new_name)

'''
while True:
    sair = input('Quer sair: [s]im ').lower().startswith('s')
    print(sair)
    

    if sair is True:
        break


