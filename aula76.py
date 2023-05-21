# len - retorna a quantidade de chaves que existe
pessoa = {
    "nome": "Geila Maria",
    "sobrenome": "Martins",
    "idade": 18,
}
print(len(pessoa))  # mostra QUANTAS chaves (QUANTIDADE)
print(pessoa.keys())  # MOSTRA as chaves que existem (EXIBE)
print(list(pessoa.keys()))  # faz a coesão para uma lista (TRANSFORMA)
print(tuple(pessoa.keys()))  # faz a coesão para uma tupla (TRANSFORMA)
print(list(pessoa.values()))  # mostra VALORES que tem
print(tuple(pessoa.items()))  # mostra

pessoa.setdefault("idade", 0)
print(pessoa["idade"])
# for chave in pessoa.keys():
#    print(chave)
