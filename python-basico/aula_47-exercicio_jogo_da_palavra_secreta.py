"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

print('----- PALAVRA SECRETA -----')
palavra_secreta = 'cachorro'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('- Digite uma letra: ')
    numero_tentativas += 1

    # Verificando se o usuário digitou apenas uma letra.
    if len(letra_digitada) > 1:
        print('-> Por favor, digite apenas uma letra!')
        continue

    # Verificando se tem a letra digitada na palavra secreta, se tiver, vai salvar na variável.
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Exibindo a letra acertada, e colocando um '*' nas outra letras para não ser exibida.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('-> Palavra formada:', palavra_formada.upper())

    # Exibindo o resultado certo e resetando o game
    if palavra_formada == palavra_secreta:
        # Importei esse módulo(os) para fazer a limpeza do terminal
        os.system('cls')
        print('--- VOCÊ GANHOU!! PARABÉNS! ---')
        print('-> A palavra era', palavra_secreta.capitalize())
        print('-> Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        break
