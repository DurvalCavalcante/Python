"""
Tipo tupla - Uma lista imutável
"""

# Dessa forma eu crio um lista imutável( que não posso mudar os valores)
nomes = 'Maria', 'Helena', 'Luiz'
print(nomes[-1])
print(nomes)

# Posso fazer dessa forma também
nome = ['Maria', 'Helena', 'Luiz']
name = tuple(nome)  # posso fazer ao contrário também (list(valor))
