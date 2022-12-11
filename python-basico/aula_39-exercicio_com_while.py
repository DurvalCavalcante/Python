"""
Iterando strings com while
"""
indice = 0
nome = "Durval Cavalcante"
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)
