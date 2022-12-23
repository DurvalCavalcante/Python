"""
Valres padrão para parâmetros
Ao definir uma função, os parâmetros pode ter valores padrão.
Caso o valor naõ seja enviado para o parâmetro, o valor padrão será usado. 
Refatorar: editar o seu código.
"""


def soma(x, y, z=0):
    if z:
        print(f'{x=} + {y=} {z=}', x + y + z)
    else:
        print(f'{x=} + {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
# o 'z' ainda não vai ser exibido, porque o '0' (zero) vai ser considerado falsy
soma(7, 9, 0)

# Aqui exibirá qualquer coisa que o usuário adicionar, mesmo que o valor seja '0'.
# Exibirá qualquer coisa que não seja None (nada)


def soma_2(a, b, c=None):  # Verificando se 'c' foi enviado
    if c is not None:
        print(f'{a=} + {b=} {c=}', a + b + c)
    else:
        print(f'{a=} + {b=}', a + b)


soma_2(7, 9, 0)
soma_2(b=9, c=0, a=7)
