frase = 'O Python é uma linguagem de programação multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

# str.count() => Retorna o número de vezes que tem aquela palavras ou letras nas strings.
# print(frase.count('Python'))

i = 0
qtd_apreceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    # Verificando se tem espaço na string, se tiver, ele vai pular(iginorar) o espaço.
    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apreceu_mais_vezes < qtd_atual:
        qtd_apreceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    '> A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apreceu '
    f'{qtd_apreceu_mais_vezes} vezes.'
)
