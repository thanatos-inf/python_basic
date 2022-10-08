# Задайте список из N элементов, заполненных числами из промежутка [-N, N].

import random

num = int(input('Введите число: '))

my_list = [random.randint(-num, num) for i in range(num)]
print(my_list)