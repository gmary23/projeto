def validar_numero():
    while True:
        try:
            numero = float(input("Insira um número: "))
            return numero
        except ValueError:
            print("Erro: Insira um número válido.")

# pedir ao usuário para inserir o primeiro número e validar
numero1 = validar_numero()

# pedir ao usuário para escolher um operador
operador = input("Escolha um operador (+, -, * ou /): ")

# pedir ao usuário para inserir o segundo número e validar
numero2 = validar_numero()

  
if operador == "+":
    resultado = num_1 + num_2
   
elif operador == "-":
    resultado = num_1 - num_2
   
elif operador == "/":
    resultado = num_1 / num_2
   
elif operador == "*":
    resultado = num_1 * num_2
  
else:
    print('Você digitou o operador inválido')

print(f'O resultado de {num_1}{operador}{num_2} é {resultado}')



