"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo conhecimentos reutilizáveis - índice e fatiamento 
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escilhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena lista
Create Read Update  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# Adiciona um item no índice escilhido .insert(índice, valor)
lista.insert(0, 5)
lista.insert(2, 15)
lista.insert(4, 25)
lista.insert(6, 35)
print(lista)
