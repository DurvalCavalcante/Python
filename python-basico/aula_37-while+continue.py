"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 50:
    contador += 1

    if contador == 5:
        print('Não vou mostrar esse número!')
        continue

    if contador >= 10 and contador <= 30:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('--- ACABOU O CONTADOR! ---')


# while contador < 50:
#     contador += 1

#     if contador % 2 == 0:
#         print(contador, 'é Par')
#     else:
#         print(contador, 'é Ímpar')

# print('--- ACABOU O CONTADOR! ---')
