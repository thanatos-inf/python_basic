# Реализуйте алгоритм перемешивания списка.

import random

num = int(input('Введите число: '))

arr = [random.randint(-num, num) for i in range(num)]
print(f'Исходный список: {arr}')

random.shuffle(arr)
print(f'"Перемашанный" список: {arr}')

