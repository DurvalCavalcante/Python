"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Aparti do momento que eu já usei os valores do enumerate, ele elimina os valores, fica como se fosse vazia
lista_enumerada = enumerate(lista)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)

# Outra forma que posso usar o enumerate sem perde os valores dele várias vezes
for itens in enumerate(lista):
    print(itens)

for itens in enumerate(lista):
    print(itens)

# Outra forma que posso usar o enumerate convertendo em uma lista ou tupla
outra_lista_enumerada = list(lista)
print(outra_lista_enumerada)

# Exibindo os valores separados com o enumerate
for valores in enumerate(lista):
    indice, nome = valores
    print(indice, nome)

# Outra forma mais simples de fazer com for
for indice_2, nome_2 in enumerate(lista):
    print(indice_2, nome_2)
