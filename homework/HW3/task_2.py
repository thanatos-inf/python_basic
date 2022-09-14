# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

def num_prod (list):
    new_list = []
    for i in range(ceil(len(list)/2)):
        list_len = len(list)
        new_num = list[i] * list[list_len - i - 1]
        new_list.append(new_num)       
    else:
        return new_list

lst = [2, 3, 4, 5, 6]
print(num_prod(lst))