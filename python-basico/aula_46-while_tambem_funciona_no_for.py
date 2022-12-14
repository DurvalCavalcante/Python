for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue  # volta pro começo do laço

    if i == 8:  # Se tirar esse if, o código vai segir até o final
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
