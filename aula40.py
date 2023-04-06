# Calculadora com while
while True:
    sair = input('Quer sair?[S]im: ').lower().startswith('s') 
    # 
    # lower ->converte tudo quer for maiúsculo para minusculo
    # sair = sair.startswith('s') -> checa se começa com s.
    if sair is True:
        print('Acabou')
        break
        
        
   

