# update atualiza e também cria

p1 = {
    "nome": "Geila",
    "sobrenome": "Martins",
}

ultima_chave = (
    p1.popitem()
)  # popitem aqui - assim como o pop, ele também busca, mas remove a última chave
print(ultima_chave)
print(p1)  # mas qdo chamamos a lista ele apagou
