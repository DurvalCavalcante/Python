"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopo internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno 
"""
x = 1  # Está no escopo global


def escopo():
    # global x  # Quando eu quiser manipular o valor de uma variável global em outro escopo
    x = 10  # Está no escopo interno da função

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()

    print(x)


escopo()
print(x)

# Tudo que é definido dentro de uma função, eu não consigo alterar de fora da função.
# Essa aula foi exibindo o código pelo debug, explicando como está funcionando cada variável.
