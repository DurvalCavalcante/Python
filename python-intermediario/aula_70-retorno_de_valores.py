"""
Retorno de valores das funções (return)
"""


def soma(x, y):  # Só posso ter um return por função, e ele só pode me retornar um valor
    if x > 10:
        return [10, 20]

    return x + y


soma_1 = soma(2, 2)
soma_2 = soma(3, 3)
print(soma_1)
print(soma_2)
print(soma(11, 55))
