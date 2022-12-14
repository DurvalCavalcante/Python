"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Durval')  # Retorna o método iter da string. __iter__()

# print(texto)
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))  # Essa dorma é igual ao de cima, eles dão o mesmo resultado

nome = 'Durval'  # Iterável
iterador = iter(nome)  # Iterador

while True:  # O for faz exatamente isso por "debaixo dos panos", sóo que mais simples
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in nome:
    print(letra)
