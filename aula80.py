"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
<<<<<<< HEAD
[1, 2, 3, 3, 2, 1], # retorna 3
[1, 2, 3, 4, 5, 6], # retorna -1
[1, 4, 9, 8, 9, 4, 8], #retorna 9
]

def encontra_primeiro_duplicado(lista_de_inteiros): # criou função para achar números inteiros
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros: # checa número por número
=======
    [1, 2, 3, 3, 2, 1],  # retorna 3
    [1, 2, 3, 4, 5, 6],  # retorna -1
    [1, 4, 9, 8, 9, 4, 8],  # retorna 9
]


def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()  # checa todos os números
    primeiro_duplicado = (
        -1
    )  # retorna o primeiro duplicado sendo "-1" sem nenhuma lógica (é uma flag)

    for numero in lista_de_inteiros:
>>>>>>> abc9d71233f272396d4506da30a6372379b8b0d1
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

<<<<<<< HEAD
        numeros_checados.add(numero)
    return primeiro_duplicado

    
for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista) # passou a lista para a função criada
    )


=======
        numeros_checados.add(numero)  # adiciona o número ao set
        print(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista))
    # if numeros in numeros_checados:
    # primeiro_duplicado =


# def encontra_primeiro_duplicado(lista_de_inteiros): # criou função para achar números inteiros
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros: # checa número por número
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)
#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista) # passou a lista para a função criada
#     )
>>>>>>> abc9d71233f272396d4506da30a6372379b8b0d1
