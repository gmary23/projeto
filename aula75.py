# Manipulando chaves e valores em dicionários

pessoa = {}

chave = "nome"

pessoa["nome"] = "Geila"
# pessoa["sobrenome"] = "Martins"

# del pessoa["sobrenome"]  # apaga o sobrenome

print(pessoa)

if (
    pessoa.get("Geila") is None
):  # o get busca dentro do IF o 'sobrenome' se não existir ele retorna "None" por padrão.
    print("NÃO EXISTE")
else:
    print("Existe sim")
