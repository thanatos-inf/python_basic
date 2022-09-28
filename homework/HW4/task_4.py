# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def list_of_koef(k):
    l_o_k = []
    for i in range(0, k + 1):
        l_o_k.append(randint(1, 100))
    return l_o_k

def polinomial(k, lst):
    first_koef = randint(1, 100)
    new_poli = f'{first_koef}*x^{k}'
    for i in range(len(lst) - 2):
        new_poli += f' + {lst[i]}*x^{k - 1}'
        k -= 1
    return new_poli + f' + {randint(1, 100)}'

k = int(input('Укажите наивысшую степень в выражении: '))

with open(r'D:\Learning\WorkFolder\py.basic\homework\HW4\file.txt', 'w') as data:
        data.write(f'{polinomial(k, list_of_koef(k))} = 0')