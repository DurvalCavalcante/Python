"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retorna um valor específico.
Por padrão, fuções Python retornam None (nada).
"""

# Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" dentro dos parênteses
# Dentro do () posso passar um parâmetro (nome de uma variável) e um valor


def saudacao(nome='Sem nome!'):
    print(f'Olá! {nome}')


# argumento é o valor passado para o parâmetro no momento da execução da função.
# Aqui eu passo o valor do meu argumento, se não passar nada, será exibido o que foi definido no parâmetro da função
saudacao('Durval')
saudacao('João')
saudacao()
