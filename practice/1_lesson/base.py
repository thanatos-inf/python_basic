#Напишите программу, которая принимает на вход два числа и проверяет,
#является ли одно число квадратом другого.

num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))

if (num_2 == (num_1 ** 2)) or (num_1 == (num_2 ** 2)):
    print(True)
else:
    print(False)


#print(type(num_1))

# num_1 = input('Введите число 1: ') /Другой вариант оформления
# num_2 = input('Введите число 2: ')

# if int(num_2) == (int(num_1) ** 2):
#     print(True)
# else:
#     print(False)
