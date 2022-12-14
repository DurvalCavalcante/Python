"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0         1
    ['Maria', 'Helena',],  # 0
    # 0
    ['Elaine',],  # 1
    # 0         1       2
    ['Luiz', 'João', 'Eduarda',],  # 2
]

# p, s, t = lista
# print(p, t)

# for nome in lista:  # Pegando cada item da lista
#     print(nome, end=' ')

# print(*lista)  # '*' Vai passar por cada um dos item de dentro da lista
# print(*string)
# print(*tupla)

print(*salas, sep='\n')  # Passando todos os valores pelo mesmo print
