while True:
# pede para digitar os números e o operador
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
#uma flag que diz que os numero são 
    numeros_validos = None

    
    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

#coloca em uma variável os operadores permitidos 
    operadores_permitidos = '+-/*'
# verifica se o operador digitado é o permitido
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
# checa se digitou apenas um operador
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
# a partir desse ponto que inicia a calculadora em si
    print('Realizando sua conta confira o resultado abaixo.')
    if operador =='+':
        print(num_1 + num_2) 
    if operador =='-':
        print(num_1 - num_2) 
    if operador =='/':
        print(num_1 + num_2) 
    if operador =='*':
        print(num_1 + num_2) 
  # aqui fala que se quiser sair basta digitar s  
    sair = input('Quer sair?[s]im: ').lower().startswith('s')

    if sair is True:
        break




