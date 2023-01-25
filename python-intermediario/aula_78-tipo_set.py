# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Durval')
s1 = set()  # vazio
s1 = {'Durval', 1, 2, 3}  # com dados

# - Sets são eficientes para remover valores duplicados de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Sets eles eliminam naturalmente os valores duplicados
exemplo_s1 = {1, 2, 3, 3, 3, 3, 3, 1}
print(exemplo_s1)
print()

# Eliminando os valores repitidos de uma lista
l1 = [1, 2, 3, 3, 3, 3, 3, 1]  # Lista
exemplo_s2 = set(l1)  # Convertendo em um set
l2 = list(exemplo_s2)  # Convertendo novamente para uma lista
print(l2)
print()

# Verificando se tem um valor no set com for
exemplo_s3 = {4, 5, 6, 7, 8}
# print(8 in exemplo_s3)
for nuemro in exemplo_s3:
    print(nuemro)

print()

# Métodos úteis:
# add, update, clear, discard

exemplo_s4 = set()
exemplo_s4.add('Durval')
exemplo_s4.add(10)
exemplo_s4.update(('Oi', 4, 5, 6))
# exemplo_s4.clear()
exemplo_s4.discard('Oi')
print(exemplo_s4)
print()

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

exemplo_s5 = {9, 8, 7}
exemplo_s6 = {8, 7, 6}

# Unindo as duas variáveis
exemplo_s7 = exemplo_s5 | exemplo_s6
print(exemplo_s7)
# Unindo é os valores repetidos serão eliminado
exemplo_s7 = exemplo_s5 & exemplo_s6
print(exemplo_s7)
# Compara os valore diferente no set e exibe o valor da esquerda
exemplo_s7 = exemplo_s5 - exemplo_s6
print(exemplo_s7)
# Era exibir os itens que não estão presente em ambos
exemplo_s7 = exemplo_s5 ^ exemplo_s6
print(exemplo_s7)
