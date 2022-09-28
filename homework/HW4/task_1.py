# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

from math import pi


edge = str(input('Введите границу округления: ')) # если указывать значение, как в условии, т.е. 0.0001
# new_edge = edge.count('0')
# print(f'π = {round(pi, new_edge)}') # через округление
value = str(pi)
new_edge_2 = int(edge.count('0'))
sliced_pi = value[0: (new_edge_2 + 2)]
print(f'π = {sliced_pi}')


# edge = int(input('Введите границу округления: ')) # если указывать границу в виде целого числа, т.е. 5
# value = str(pi)

# print(f'π = {round(pi, edge)}') # через округление
# sliced_pi = value[0: (edge + 2)] # через срез
# print(f'π = {sliced_pi}')