# 1. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

# import time

# for i in range(10):
#     a = time.time()


# 2. Задайте список. Напишите программу, которая определит, присутствует ли 
# в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"

n_list = ['65h34q', 'sdg634d', '147jnbv']

n = int(input('Введите число: '))
n1 = str(n)

for i in range(len(n_list)):
    str1 = n_list[i]
    a = str1.find(n1)
    #print(a)
    if (a >= 0):
        print(f'В строке {i+1} списка содержится число "{n1}"')

# 2 вариант

# n = 'h'  
# mylist = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']
# def find_number(n, lst):
#     res = []
#     for i in lst:
#         if n in i:
#             res.append(i)
#     return res
# print(find_number(n, mylist))



# 3. Напишите программу, которая определит позицию второго вхождения строки в 
# списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# new_list = ["1", "qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# # new_string = 'qwe'
# new_string = n = str(input('Введите элемент: '))
# count = 0
         
# for i in range(0, len(new_list)):
#     if new_list[i] == new_string:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# if count < 2:
#     print("Такой элемент отсутствует")

# my_list = ["qwe", "asd", "zxc", "ertqwe", 'qwe']
# value = 'qwe1'
# count = 0
# n_bool = False
# for i in range(len(my_list)):
#     if value == my_list[i]:
#         count += 1
#         if count == 2:
#             print(i)
#             n_bool = True
# if n_bool == False:
#     print('Такой элемент отсутствует')
