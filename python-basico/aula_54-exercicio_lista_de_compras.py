"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

"""
Minha lógica (funcionou)

lista_de_compras = []

while True:
    print('--- Selecione uma opção ---')
    digitar = input('[i]nserir [a]pagar [l]ista: ')

    if digitar == 'i' or digitar == 'I':  # Adicionando o item na lista
        os.system('cls')
        inserir = input('-> Insira o item: ')
        lista_de_compras.append(inserir)

    if digitar == 'l' or digitar == 'L':
        if lista_de_compras == []:
            os.system('cls')
            print('-> Nada para listar!')

        if lista_de_compras != []:
            os.system('cls')
            for indice_lista, nome_lista in enumerate(lista_de_compras):
                print(indice_lista, nome_lista.capitalize())

    if digitar == 'a' or digitar == 'A':
        try:
            apagar = input('-> Escolha o índice para apagar: ')
            convertion_apagar = int(apagar)

            if convertion_apagar == indice_lista:
                del lista_de_compras[convertion_apagar]
            else:
                print('-> Não foi possível apagar o índice!')
        except ValueError:
            print('-> Não foi possível apagar o índice!')
            continue
"""


lista = []

while True:
    print('--- Selecione uma opção ---')
    opcao = input('[i]nserir [a]pagar [l]ista: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('-> Valor: ')
        lista.append(valor.capitalize())
    elif opcao == 'a':
        indice_str = input('-> Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('-> Não foi possível apagar este índice!')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('-> Nada para listar!')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('-> Por favor, escolha i, a ou l.')
