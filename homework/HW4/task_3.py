# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def unique(lst):
    new_list = []
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            new_list.append(lst[i])
    return new_list

my_list = [1, 1, 2, 3, 4, 5, 5]

print(unique(my_list))


