"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0


while True:# aqui manda executar a função até as opções serem verdadeiras
    letra_digitada = input('Digite uma letra: ') # manda digitar uma letra 

    if len(letra_digitada) > 1: # aqui 
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta: # verifica se a letra digitada está dentro da variável armazenada
            letras_acertadas += letra_digitada # a variável "letra_acertada" soma com a letra que foi digitada
            #print(letras_acertadas)

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
             print(letra_secreta)
        
        #for letra in letra_secreta:
            #print('Parabéns você digitou a palavra secreta')