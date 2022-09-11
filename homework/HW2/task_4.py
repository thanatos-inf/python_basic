# Задайте список из N элементов, заполненных числами из промежутка [-N, N].

import random

num = int(input('Введите число: '))

arr = [random.randint(-num, num) for i in range(num)]
print(arr)