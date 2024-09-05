"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')


###################### PARTE 2


Operadores de atribuição
= += -= *= /= //= **= %=

contador = 10


contador /= 5
print(contador)


####################### PARTE 3



Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')
"""