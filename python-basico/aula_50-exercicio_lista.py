"""
Exercício
Exiba os índices da lista
"""

"""
Minha lógica

lista = ['Maria', 'Helena', 'Luiz']
i = 0

while i < len(lista):

    for nome in lista:
        print(i, nome)
        i += 1
"""
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])
