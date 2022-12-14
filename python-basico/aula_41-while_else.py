""" while/else """
string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    # Toda vez que tiver um break, o else não será executado. Caso contrário, o else será executado.
    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')

print('Fora do while.')
