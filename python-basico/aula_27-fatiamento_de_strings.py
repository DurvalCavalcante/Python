"""
Fatiamento ded strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] i-(início) f-(fim) p-(passo) - de quantos caracteres ele vai pular. 
Obs.: a função len retorna a qauntidade de caracteres da strings
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[0:5])
print(variavel[-8:-2])
print(variavel[0:9:1])
print(variavel[::-1])  # invertido
print(len(variavel))
