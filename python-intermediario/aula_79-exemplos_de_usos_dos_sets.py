# Exemplo de uso dos sets

letras = set()

print('- Encontre a letra correta')
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'c' in letras:
        print('- Parabéns!!! A letra correta era "', letra, '"')
        break

    print(letras)
