# Operadores uteis
# '|' união
# '&' intersecção
# '-' diferença
# '^' diferença simetrica

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # Une tudo, mas remove o que tem repetido.
s4 = s1 & s2  # intersecção - mostra os itens presentes em ambos.
s5 = s1 - s2  # mostra o único elemento presente no set da esquerda(1).
s6 = (
    s2 - s1
)  # mudando de posição mostra também o que está presente no set da esquerda (4).
s7 = s1 ^ s2  # mostra o que não estão presentes em ambos(1, 4), sem importar a ordem.


print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
