# or --> Combina duas condições ou expressões e 
# retorna se pelo menos uma delas for verdadeira
# A condição pára quando encontrar algo verdadeiro (operação conhecida como curto circuito)
entrada = input('[E]ntrar [S]air')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada =='e') and senha_digitada == senha_permitida:


    print('Entrar ')
else:
    print('Sair ')