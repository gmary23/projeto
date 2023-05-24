# len - retorna a quantidade de chaves que existe
pessoa = {
    "nome": "Geila Maria",
    "sobrenome": "Martins",
}
print(len(pessoa))  # mostra QUANTAS chaves (QUANTIDADE)
print(pessoa.keys())  # MOSTRA as chaves que existem (EXIBE)
print(list(pessoa.keys()))  # faz a coesão para uma lista (TRANSFORMA)
print(tuple(pessoa.keys()))  # faz a coesão para uma tupla (TRANSFORMA)
print(list(pessoa.values()))  # mostra VALORES que tem
print(tuple(pessoa.items()))  # mostra as chaves e os valores

pessoa.setdefault(
    "idade", 140
)  # serve para mostrar uma idade qdo não foi colocada no dicionário
print(pessoa["idade"])


# for chave in pessoa.keys():
#    print(chave)
