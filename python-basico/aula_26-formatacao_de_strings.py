"""
Formatação básica de strings
S - string
d - int
f - float
.<números de dígitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esqquerda
< - Direita
^ - Centro
= - força o número a aparecer antes do zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->11}')
print(f'{variavel:-<11}')
print(f'{variavel:-^11}')
print(f'{1000.4877417247427:,.1f}')
print(f'{1000.4877417247427:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
