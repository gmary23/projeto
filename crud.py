import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]serir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')

    elif opcao == 'a':
        indice_str = input('Escolha uma pção para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except:
            ...

    elif opcao == 'l':
        print('l')


'''
while True: # 
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        print('a')

    elif opcao == 'l':
        os.system('clear')

        if lista == 0:
            print('A lista não tem nada')

            for indice, valor in enumerate(lista):
                print(indice, valor)
        print('l')

        '''
