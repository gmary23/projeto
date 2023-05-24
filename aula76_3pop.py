# pop apaga um item com a chave especificada (del) -
# é tipo del, mas tem algo a mais

p1 = {
    "nome": "Geila",
    "sobrenome": "Martins",
}

nome = p1.pop("nome")  # pop aqui - ele busca o nome
print(nome)
print(p1)  # mas qdo chamamos a lista ele apagou
