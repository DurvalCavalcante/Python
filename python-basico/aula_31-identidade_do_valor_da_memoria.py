"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
print(id(v1))  # Para olha a identidade de um elemento na memória

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('- Faça algo')
else:
    print('- Não faça algo')

# Retonar verdadeiro quando a variável for None
print(passou_no_if, passou_no_if is None)
# Retorna falso quando a variaável não for None
print(passou_no_if, passou_no_if is not None)


if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
