"""
Cuidados com dados mutáveis 
= - Copiado o valor (imutáveis)
= - Aponta para o mesmo valor na memória (mutável)
"""
# Dessa forma eu estou alterando os itens da primeira variável também
lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)

# Copiando os valores de uma lista para outra variável
lista_c = ['Luiz', 'Maria', 1, True, 1.2]
lista_d = lista_c.copy()  # Fazendo uma copia dos valores da lista_c

lista_c[0] = 'Qualquer coisa'
print(lista_c)
print(lista_d)
