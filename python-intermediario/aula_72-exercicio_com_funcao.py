# Exercício com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*args):
    total = 1

    for numero in args:
        total *= numero

    return total


resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)


# Crie uma função fala se um número é pra ou ímpar.
# Retorne se o número é pra ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é Par!'
    else:
        return f'{numero} é Ímpar!'


print(par_impar(3))
print(par_impar(6))
print(par_impar(9))
print(par_impar(12))
