"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('- Vou dobrar o número que você digitar: ')

# if numero_str.isdigit():  # .isdigit() =>   Checa se o usuário digitou apenas números.
#     numero_convertion = float(numero_str)
#     print(f'> O dobro de {numero_str} é {numero_convertion * 2}')
# else:
#     print('- Isso não é um número!')

try:
    numero_convertion = float(numero_str)
    print(f'> O dobro de {numero_str} é {numero_convertion * 2}')
except:
    print('- Isso não é um número!')

# try/except => Você consegue capturar o erro na exceção
