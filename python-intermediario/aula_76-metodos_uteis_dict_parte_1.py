# Métodos úteis dos dicionários em Python
# len - Quantas chaves
# keys - Iterável com as chaves
# values - Iterável comos valores
# items - Iterável com chaves e valores
# setdefault - Adiciona valor se a chave não existe
# copy - Retorna uma cópia rasa (shallow copy)
# get - Obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Durval',
    'sobrenome': 'Cavalcante',
}

print(len(pessoa))  # Tamanho
print()

print(list(pessoa.keys()))  # Chaves
for chave in pessoa:
    print(chave)
print()

print(list(pessoa.values()))  # Valores
for valor in pessoa.values():
    print(valor)
print()

print(list(pessoa.items()))  # Chave e valor
for chave, valor in pessoa.items():
    print(chave, valor)
print()

# Adicionar um valor padrão se não estiver no dicionário
pessoa.setdefault('idade', 18)
print(pessoa['idade'])
print()
