perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "opcoes_resp": ["1", "2", "4", "6"],
        "Resposta:": "4",
    },
    {
        "Pergunta": "Quanto é 2*3?",
        "opcoes_resp": ["2", "4", "6", "8"],
        "Resposta:": "4",
    },
]
qtd_acertos = 0
for perg in perguntas:
    print(perg["Pergunta"])  # puxa quantas perguntas tiverem
    print()  # gera espaço

    opcoes = perg["opcoes_resp"]
    for i, opcoes in enumerate(opcoes):
        print(f"{i})", opcoes)
    print()

    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():  # verifica se digitou um número inteiro
        escolha_int = int(escolha)

    if escolha_int is not None:  # se escolheu um dígito
        if (
            escolha_int >= 0 and escolha_int < qtd_opcoes
        ):  # verifica se escolhe a quantidade correta de opções
            if opcoes[escolha_int] == perg["Resposta"]:
                acertou = True

    if acertou:
        qts_acertos = +1
        print("Acertou")
    else:
        print("Errou")
        ...

    print()  # gera espaço

print("Você acertou", qtd_acertos)
print("de", len(perg), "perguntas")
