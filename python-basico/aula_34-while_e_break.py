"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('- Qual é o seu nome: ')

    if nome == 'sair' or nome == 'Sair':
        break
    else:
        print(f'> Seu nome é {nome}')

print('--- ACABOU! ---')
