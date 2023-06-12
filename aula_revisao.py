palavra = input("Digite uma palavra: ") # a variável receberá a palavra digitada
mais_repetida = None # guarda a letra que mais se repete 
maior_frequencia = 0 # guarda a frequência que se repete
i = 0
while i < len(palavra):
    letra = palavra[i]
    #print(letra, i)
    frequencia = palavra.count(letra) # conta quantas vezes ela aparece na palavra e armazena na variável frequên
    if frequencia > maior_frequencia: #
        mais_repetida = letra
        maior_frequencia = frequencia
    i += 1
print(f"A letra que mais se repete é {mais_repetida}, {maior_frequencia} vezes.")