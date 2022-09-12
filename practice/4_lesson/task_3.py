# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

import math

import math
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
print(f'НОК: {math.lcm(num_1, num_2)}')

with open('file.txt', 'w') as f:
    f.write(str(math.lcm(num_1, num_2)))
