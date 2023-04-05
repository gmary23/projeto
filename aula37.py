contador = 0 # a contagem começa a partir do 

while contador <= 100: # diz que vai até 100, mas só +1 e mostra até 101
    contador += 1 #começa a fazer a conta (então soma 0+1)

    if contador == 6: #diz que qdo chegar no 6 ñ mostrar
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27: #diz que entre o 10 e 27 não mostrar
        #print('Não vou mostrar o 6.')
        continue
     
    print(contador)
    
    if contador == 40: # fala que quando chegr em 40 parar
        break

print('Acabou')