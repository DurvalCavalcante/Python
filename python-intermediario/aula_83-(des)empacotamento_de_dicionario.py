# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)
print()

# Empacotamento
# a, b = pessoa.values()  # Retorna só os valores
# print(a, b)
# print()

# a, b = pessoa.items()  # Retorna os itens
# print(a, b)
# print()

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Durval',
    'sobrenome': 'Cavalcante'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

# Desempacotamento
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
print()

# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumento_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print('Nomeados:', chave, valor)


mostro_argumento_nomeados(1, 2, nome='João', sobrenome='Silva')
print()
mostro_argumento_nomeados(**pessoa_completa)
print()
