"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo conhecimentos reutilizáveis - índice e fatiamento 
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE'  # 5 caracteres

#               Índices
#         0     1      2       3    4
#        -5    -4     -3      -2   -1
lista = [123, True, 'Durval', 1.2, []]
lista[2] = 'Durval Cavalcante'  # Mudando o valor do índice
print(lista)
print(lista[2], type(lista[0]))
