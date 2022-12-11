"""
1- Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número interioro.
"""
numero = input('- Digite um número inteiro: ')

if numero .isdigit():
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print(f'> Seu número {numero_int} é Par.')
    else:
        print(f'> Seu número {numero_int} é Ímpar.')

else:
    print('- Por favor, digite apenas números inteiros')

"""
Outra Forma de fazer o primeiro exercício

numero = input('- Digite um número inteiro: ')

try:
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'> O número {numero_int} é {par_impar_texto}')
except:
    print('- Você não digitou um números inteiro')
"""

"""
2- Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""
"""
--- Minha lógica ---

horario = input('- Digite a hora em números inteiros: ')

try:
    horario_convertion = int(horario)
    if horario_convertion <= 11:
        print('> Bom dia!')
    elif horario_convertion <= 17:
        print('> Boa tarde!')
    else:
        print('> Boa noite!')
except:
    print('- Digite um númeor inteiro')
"""

hora_digitada = input('- Digite a hora em números inteiros: ')

try:
    hora = int(hora_digitada)
    if hora >= 0 and hora <= 11:
        print('> Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('> Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('> Boa noite!')
    else:
        print('- Não conheço essa hora!')
except:
    print('- Por favor, digite apenas números inteiros!')


"""
3- Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é grande".
"""

"""
--- Minhha lógica ---

nome = input('- Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('> Seu nome é curto')
elif len(nome) <= 6:
    print('> Seu nome é normal')
else:
    print('> Seu nome é muito grande')

"""
nome = input('- Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('> Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('> Seu nome é normal')
    else:
        print('> Seu nome é muito grande')

else:
    print('- Por favor, digite mais de uma letra!')
