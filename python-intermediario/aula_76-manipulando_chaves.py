# Manipulando caves e valores em dicionários

dados = {}

dados['nome'] = 'Durval'  # Criando uma chave com o sinal de atribuição (=)

print(dados)
print(dados['nome'])

# .get => Retorna o valor da chave se a chave estiver no dicionário, caso contrário, é padrão (None).
if dados.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(dados['sobrenome'])


"""
dados = {}

chave = 'nome' # Criando uma chave dinâmica

dados[chave] = 'Durval' # Acessando a chave
dados['sobrenome'] = 'Cavalcante'
print(dados[chave])

dados[chave] = 'João' # Trocando o valor da chave
del dados['sobrenome'] # Apagando o valor da chave
print(dados)
"""
