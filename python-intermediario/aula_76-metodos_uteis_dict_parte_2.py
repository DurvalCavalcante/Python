p1 = {
    'nome': 'Durval',
    'sobrenome': 'Cavalcante',
}

print(p1['nome'])

# .get - Verificando se tem 'nome' no dicionário
print(p1.get('nome', 'Não existe'))
print()

# .pop - Retornar o valor e elimina a chave do dicionário
nome = p1.pop('nome')
print(nome)
print(p1)
print()

p2 = {
    'nome': 'João',
    'sobrenome': 'Da Silva',
}

# .popitem - Retornar o valor e elimina a última chave do dicionário
ultima_chave = p2.popitem()
print(ultima_chave)
print(p2)
print()

p3 = {
    'nome': 'Maria',
    'sobrenome': 'Ramos',
}
print(p3)

# .update - Atualiza as chaves do dicionário e podem ser criadas outras chaves
p3.update({
    'nome': 'Joana',
    'idade': 30,
})
print(p3)
print()

# Outras formas de usar o .update
p3.update(nome='Priscila', idade=20)
print(p3)
print()

tupla = ('nome', 'Bruna'), ('idade', 24)
# lista = [['nome', 'Bruna'], ['idade', 24]] # Com a lista é a mesma coisa da tupla
p3.update(tupla)
print(p3)
