"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo conhecimentos reutilizáveis - índice e fatiamento 
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
print(lista)

lista[2] = 300  # Alterando o valor da lista pelo índice
print(lista)

del lista[2]  # Apagando um índice e o item da lista
print(lista)

lista.append(50)  # Adicional um item no final da lista
print(lista)

ultimo_valor = lista.pop()  # Remove o último item da lista
print(lista, 'Removido', ultimo_valor)
