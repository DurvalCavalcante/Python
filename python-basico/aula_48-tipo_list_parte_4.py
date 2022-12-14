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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Concatena lista
lista_c = lista_a + lista_b
print(lista_c)

# Estende a lista na variável escolhida, não posso pegar esse valor é jogar em outra variável
lista_a.extend(lista_b)
print(lista_a)
