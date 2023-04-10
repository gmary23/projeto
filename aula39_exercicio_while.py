
nome = 'Vitor Martins'

indice = 0 # aqui é zero pq quero que inicie da primeira letra
novo_nome = '' # essa strig é vazia pq quero que comece do nada

while indice < len(nome): # aqui começa pegar pelo indice zero
    letra = nome[indice] # aqui pega a letra pelo nome e pelo índice
    novo_nome += letra # aqui o novo_nome que está fazio agora recebe a primeira letra do nome e armazena
    indice += 1 # agora o indice lá de cima não entra mais e esse passa a somar com + 1. Até finalizar as letras

print(novo_nome) # aqui impre o novo_nome

