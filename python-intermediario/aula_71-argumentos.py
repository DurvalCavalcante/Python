"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):  # args - é usado para passar um quantidade ilimitada de argumentos
    total = 0
    for nuemro in args:
        total += nuemro

    return total


soma_1_2_3 = soma(1, 2, 3,)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6,)
print(soma_4_5_6)

numeros = 7, 8, 9, 10, 11, 12, 13
outra_soma = soma(*numeros)  # Desempacotando a tupla para funcionar na função
print(outra_soma)

# sum - Retorna a soma de um valor 'inicial' (padrão: 0) mais um iterável de números
print(sum(numeros))
