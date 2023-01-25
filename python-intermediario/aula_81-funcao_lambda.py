"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha.
Ou seja, tudo deve ser contido dentro de uma única expressão.
    lista = {
        {'nome': 'Durval', 'sobrenome': 'Cavalcante'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome': 'Aline', 'sobrenome': 'Souza'},
    }
"""
# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort()  # A lista vai ser ordenada
# print(lista)
# print()

# lista.sort(reverse=True)  # Mudando a ordem
# print(lista)
# print()

lista = [
    {'nome': 'Durval', 'sobrenome': 'Cavalcante'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

"""
Outro exemplo:
def ordena(item):  # Ordenando a lista por ordem de nome
    return item['nome']

lista.sort(key=ordena)  # Passando a função para ser ordenada
"""

# lista.sort(key=lambda item: item['nome'])

# for item in lista:  # Passando pela lista em ordem
#     print(item)


def exibir(lista):
    for item in lista:
        print(item)

    print()


# sorted() - Retorna uma cópia da lista, mas uma cópia rasa
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
