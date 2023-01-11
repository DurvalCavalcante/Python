import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = d1.copy()

d2['c1'] = 100
# Alterando uma lista no dicionário mesmo sendo uma cópia, ele sempre vai alterar o dicionário principal.
d2['l1'][1] = 9

print(d1)
print(d2)
print()

d3 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d4 = copy.deepcopy(d3)  # Dessa forma não altera o dicionário principal

d4['c1'] = 10
d4['l1'][1] = 900

print(d3)
print(d4)
