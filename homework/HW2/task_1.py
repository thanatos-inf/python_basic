# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 0,56 -> 11

num = (input('Введите вещественное число: '))
splited_num = num.split('.')
# splited_num = num.split(',')
num_left = int(splited_num[0])
num_right = int(splited_num[1])
result = 0
while (num_left != 0):
    result += (num_left % 10)
    num_left = num_left // 10
while (num_right != 0):
    result += (num_right % 10)
    num_right = num_right // 10

print(result)




