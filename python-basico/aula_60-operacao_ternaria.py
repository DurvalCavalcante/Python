"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(f'{variavel}\n')

digito = 9
novo_digito = digito if digito <= 9 else 0
outro_digito = 0 if digito > 9 else digito
print(f'{novo_digito}\n')
print(outro_digito)
