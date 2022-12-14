"""
Introdução ao desempacotamento + tuples (tuplas)
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome_1, nome_2, nome_3 = nomes  # Criando 3 variáveis para cada um item da lista
print(nome_1, nome_2, nome_3)

# Posso fazer dessa forma também. Sempre crira as quantidades de variáveis conforme a lista
nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']


# Pegando um item com uma variável só de uma lista
# '*' siginifa que ele vai empacotar o resto dos itens da lista
# '_' o underline significa uma variável que eu não vou usar, mas ela funciona normal
_, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, _, resto)
