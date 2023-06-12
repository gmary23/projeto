valor = int(input('Quanto valo do empréstimo? '))
parcelas = int(input('Quantas parcelas? '))
resultado = (valor*20)/100
total = resultado + valor
final = (valor+resultado)/parcelas

print(f'O valor total do empréstimo é {total}')
print(f'O valor das parcelas é: {final}')