"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
# Exemplo de como posso alterar caracteres de uma string
string = 'Durval Cavalcante'
outra_variavel = f'{string[:3]}VAL{string[6:]}'
print(string)
print(outra_variavel)

# srt.capitalize() => Retorma uma cópia da string com seu primeiro caractere em maiúsculo e o retante em minúsculo
nome = 'durval'
sobrenome = 'cavalcante'

print(nome.capitalize(), sobrenome.capitalize())

# str.zfill() => Retorna uma cópia da String deixada preenchida com dígitos '0' para fazer uma string de comprimento width
string_2 = '1000'

# Preenche até chegar ao número de caractere informado
print(string_2.zfill(50))
