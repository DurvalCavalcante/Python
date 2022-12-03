# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  D u r v a l
# -6-5-4-3-2-1

# nome = 'Durval'

# print(nome[4])
# print(nome[-2])
# print(20 * '-')
# print('a' in nome)
# print('w' in nome)
# print(20 * '-')
# print('val' not in nome)
# print('silva' not in nome)

nome = input('- Digite seu nome: ')
encontrar = input('- Digite qual letra do seu nome você deseja encontrar: ')

if encontrar in nome:
    print(f'> {encontrar} está em {nome}')
else:
    print(f'> {encontrar} não está em {nome}')
