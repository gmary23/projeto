# usar a função count para contar na frase
frase = 'Essa é uma frase que estou usando para guardar uma variável e estudar python'

#.upper()
#print(frase)
#print(frase.count('python')) # mostra quantas vezes o nome python apareceu na frase

i = 0 #começa no zero
while i < len(frase): #enquanto o indice for menor que o tamanho da frase ou a frase toda
    letra_atual = frase[i] # a variável letra recebe o índice da frase, ou seja comença contar os números 
    qtas_vezes_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, qtas_vezes_letra_apareceu) # mostra a letra atual
    i += 1 # aqui começa a juntar e volta para o while e faz tudo novamente
