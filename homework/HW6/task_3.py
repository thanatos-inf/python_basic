# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

num = int(input('Введите число: '))

item  = lambda k: (1 + 1/k)**k
my_list = [item (i + 1) for i in range(num)]

result = 0
for i in range(num):
    result += my_list[i]

print(round(result, 4))