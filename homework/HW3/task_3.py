# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

from math import *

def max_min (list):
    result = max(list) - min(list)
    return result

lst = [1.1, 1.2, 3.1, 10.01]
new_list = []

for item in range(len(lst)):
    new_item = round(float(lst[item] - round(lst[item])), 2)
    new_list.append(new_item)
    
print(f'{lst} => {round(max_min(new_list), 2)}')

