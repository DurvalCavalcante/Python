# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('- Senha: ')

if senha == '123456':
    print('> Entrou')
else:
    print('> Senha incorreta.')

senha_1 = input('- Senha: ')

if senha_1 != '123456':  # Checar a senha incorreta primeiro
    print('> Senha incorreta.')

senha_2 = input('- Senha: ')

if not senha_2:  # Quando o usuário não digitar nada
    print('> Você não digitou nada')
