"""
Imprecisão de ponto flutuante
Double-presision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numeros_1 = 0.1
numeros_2 = 0.7
numeros_3 = numeros_1 + numeros_2
print(numeros_3)
print(f'{numeros_3:.2f}')
# round() -> Ele arredondar um número para uma determinada precisão em dígitos decimais.
print(round(numeros_3, 2))

# Tem como fazer dessa forma também, importando o decimal
numeros_4 = decimal.Decimal('0.2')
numeros_5 = decimal.Decimal('1.6')
numeros_6 = numeros_4 + numeros_5
print(numeros_6)
print(f'{numeros_6:.2f}')
print(round(numeros_6, 2))
