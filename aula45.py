'''
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu interador
'''
# for letra in texto
texto = 'Luiz' #iterável

iteratador = iter(texto) 

#while True:
#   try:
#      letra = next(iteratador)
#        print(letra)
#    except StopIteration:
#        break

# O exemplo acima mostra como o "for" funciona por baixo dos panos
# que é o mesmo que esse exemplo abaixo faz

for letra in texto:
    print(letra)


