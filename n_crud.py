import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('clear')  # limpa o terminal
        valor = input('Valor: ')  # inclui valor
        lista.append(valor)  # esse item insere item na lista

    elif opcao == 'a':
        apaga = input('Escolha um item para apagar: ')

        indice = int(apaga)
        del lista[indice]
        # IndexError

    elif opcao == 'l':

        if len(lista) == 0:
            print('Lista vazia')

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Selecione a opçao informada')
