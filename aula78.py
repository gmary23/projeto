# sets - são semelhantes ao conjuntos ensinados na matemática
# Eles são:
# iteráveis;
# Não garantes ordem dos elementos
# Não possuem índexes
# Removem valores duplicado
# Não aceitam valores mutáveis

s1 = set("Geila")  # são iteráveis
s2 = set(("Geila", 1, 2, 4, 4))  # se acrescentar () lê como string.
s3 = set("teste")


s2.add("Luiz")  # adicionou informação nesse set
s2.update(
    (
        "Olá mundo",
        1000,
    )
)  # como foi inserido uma tupla precisa uma vírgula no final
s3.clear()  # limpou toda informação que tem em s3
s2.discard(2)  # removeu apenas o número(2) informado da lista s2


print(s1)
print(s2)
print(s3)
