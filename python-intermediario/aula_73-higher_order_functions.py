"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions (Funções de primeira) - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia!', 'Durval'))
print(executa(saudacao, 'Bom dia!', 'Maria'))
