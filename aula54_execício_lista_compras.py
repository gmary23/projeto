import os  # esse comando manda importar comando do sistema operacional em algum momento no código
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]serir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        lista.remove(valor)
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('nada para lista')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        os.system('clear')
        print('Por favor, escolha i, a ou l')
