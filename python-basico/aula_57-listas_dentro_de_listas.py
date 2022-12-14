"""
Lista de lista e seus índices
"""

salas = [
    # 0         1
    ['Maria', 'Helena',],  # 0
    # 0
    ['Elaine',],  # 1
    # 0         1       2
    ['Luiz', 'João', 'Eduarda',],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])

for sala in salas:  # Vai retornar todas as lista dentro da variável sala
    print(f'-> A sala é {sala}')
    for aluno in sala:  # Vai retorna os valores dos índice de cada lista
        print(f'{aluno}')
