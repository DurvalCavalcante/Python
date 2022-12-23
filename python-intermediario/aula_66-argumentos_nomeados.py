"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados te nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""


def soma(x, y):
    # Definição
    print(f'{x=} y={y}', '|', 'x + y =', x + y)


# Argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.
soma(1, 2)
soma(2, 1)
soma(y=2, x=1)  # Argumentos nomeados recebem o nome do parâmetro antes do valor
