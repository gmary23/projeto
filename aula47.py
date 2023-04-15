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
    letra_digitada = input('Digite uma letra: ') # manda digitar uma letra e colocar na variável "letra_digitada"
    numero_tentativas += 1 

    if len(letra_digitada) > 1: # aqui lê a quantidade de letras que foram digitada e se tiver sido digitada mais de um, manda digitar apenas 1.
        print('Digite apenas uma letra')
        continue # essa função manda voltar ao início até que seja verdadeiro

    if letra_digitada in palavra_secreta: # verifica se a letra digitada está dentro da variável armazenada
            letras_acertadas += letra_digitada # a variável "letra_acertada" soma com a letra que foi digitada
            #print(letras_acertadas)

    palavra_formada = '' #criou uma váriavel para armazenar as palavras que começou a ser formada
    for letra_secreta in palavra_secreta: # o for criou uma variável sem precisar declarar no início e fala se a palavra_secreta em palavra_secreta, então...
        if letra_secreta in letras_acertadas: # cria a lógica
            palavra_formada += letra_secreta  # pega a palavra formada + a letra_secreta
        else:
             palavra_formada += '*' # se não tiver a letra na palavra mostra um "*"
    print('Palavra formada:', palavra_formada) # vai mostrando a palavra que está se formando

    if palavra_formada == palavra_secreta:          
         print('Parabéns você ganhou!')
         print('A palavra era' , palavra_secreta)
         print('Tentativas', numero_tentativas)
         
        
        