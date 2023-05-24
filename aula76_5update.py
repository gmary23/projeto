# update atualiza e também cria

p1 = {
    "nome": "Geila",
    "sobrenome": "Martins",
}

p1.update(
    {
        "nome": "João",
        "idade": "32",  # criou uma idade que não existia
    }
)  # atualizou o nome na lista
print(p1)

###############
# Outra forma de usar update é usar valores nomeados, como no exemplo abaixo.
p1.update(nome="Vitor", idade="11")
print(p1)
