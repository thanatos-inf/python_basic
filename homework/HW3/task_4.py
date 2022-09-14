# Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ten_to_two(number):
    dec = []
    while (number > 0):
        new_num = number % 2
        number = number // 2 
        dec.insert(0, new_num)       
    return dec

def string_form(string):
    for i in string:
        print(i, end = '')

num = int(input('Введите число: '))

print('Введённое Вами число в двоичной системе выглядит так: ')
# print(*ten_to_two(num))
string_form(ten_to_two(num))
