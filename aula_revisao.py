palavra = input('Digite uma palavra: ')
mais_repete = None
maior_frequencia = 0
i = 0

while i < len(palavra):
    letra = palavra[i] # criou a variável "letra" que recebe a palavra e o índice
    frequencia = palavra.count(letra) # a variável frequencia recebe a contagem das palavras
    print(frequencia)
    if frequencia > maior_frequencia:
        mais_repete = letra 
        maior_frequencia = frequencia  
    i += 1

print(f'A palavra que mais se repete é "{mais_repete}"  se repete {maior_frequencia}x')

# palavra = input("Digite uma palavra: ") # a variável receberá a palavra digitada
# mais_repetida = None # guarda a letra que mais se repete 
# maior_frequencia = 0 # guarda a frequência que se repete
# i = 0
# while i < len(palavra):
#     letra = palavra[i]
#     #print(letra, i)
#     frequencia = palavra.count(letra) # conta quantas vezes ela aparece na palavra e armazena na variável frequên
#     if frequencia > maior_frequencia: #
#         mais_repetida = letra
#         maior_frequencia = frequencia
#     i += 1
# print(f"A letra que mais se repete é {mais_repetida}, {maior_frequencia} vezes.")