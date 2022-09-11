# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

num = int(input('Введите число: '))
result = 0
my_list = []

def new_num(n):
    return ((1 + 1/n)**n)

for i in range(1, num+1):
    my_list.append(round(new_num(i), 4))

for i in range(1, num+1):
    result += new_num(i)

print(f'Последовательность значений представлена в списке: {my_list}')
print(f'Сумма чисел последовательности составляет: {round(result, 4)}')
