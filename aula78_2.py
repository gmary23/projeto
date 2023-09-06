# Exemplos de uso de sets
# Exemplo de uso de sets
letras = set()
while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if "l" in letras:
        print("PARABENS VOCÊ DIGITOU A LETRA CORRETA")
        break

    print(letras)
