"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número rececbido como parâmetro.
"""

"""
Minha lógica do exercício funcionando

digitando = input('Digite um número: ')


def duplicando(numero):

    return f'Duplicando = {int(numero) * 2}'


def triplicando(numero):

    return f'Triplicando = {int(numero) * 3}'


def quadruplicando(numero):

    return f'Quadruplicando = {int(numero) * 4}'


print(duplicando(digitando))
print(triplicando(digitando))
print(quadruplicando(digitando))
"""

# Lógica do curso

digitar = input('Digite um número: ')


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(int(digitar)))
print(triplicar(int(digitar)))
print(quadruplicar(int(digitar)))
