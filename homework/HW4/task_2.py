# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def list_of_simples(num):
    full_list = [2, 3, 5, 7]
    list_of_simp = []
    for item in range(2, num):
        if (item % 2 != 0) and (item % 3 != 0) and (item % 5 != 0) and (item % 7 != 0):
            list_of_simp.append(item)
    return full_list + list_of_simp

def simple_multipiers(number, sim_list):
    simple_list = sim_list
    multipliers = []
    for i in simple_list:
        for j in simple_list:
            if (number % j == 0):
                multipliers.append(j)
                number /= j
                break
    return multipliers

simple_list = list_of_simples(int(input('Введите границу для списка простых чисел: ')))
number = int(input('Введите число: '))

print(f'Простые множители введённого Вами числа: {simple_multipiers(number, simple_list)}')
