"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
# Dessa forma o split vai divide a string aonde tiver espaço
lista_palavras = frase.split()
print(f'{lista_palavras}\n')

# Posso passar o caractere dentro do split para informa onde eu quero divide a string
lista_frase = frase.split(', ')  # Dividindo aonde tem vírgula e espaço
print(f'{lista_frase}\n')

# Um exemplo com for
for i, frase in enumerate(lista_frase):
    # .strip() -> Corta os espaços do começo e do fim da string
    print(f'{lista_frase[i].strip()}\n')

#
frase_2 = 'Outro exemplo, diferente'
lista_frases_cruas = frase_2.split(',')

lista_frase_2 = []
for indice, frase_2 in enumerate(lista_frases_cruas):
    lista_frase_2.append(lista_frases_cruas[indice].strip())

print(f'{lista_frases_cruas}\n')
print(f'{lista_frase_2}\n')

# É na primeira string que vamos add o que queros separa a string, depois add o .join() e a string que quermos separar
frase_unidas = '-'.join(lista_frase_2)
print(frase_unidas)
