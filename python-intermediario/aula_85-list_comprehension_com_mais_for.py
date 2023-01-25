lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [  # É igual ao de cima
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
