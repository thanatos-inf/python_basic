# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from audioop import reverse

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

num = int(input('Введите число: '))
my_list = []

for i in range(1, num + 1):
    my_list.append(fib(i))
    
rev_list = list(reversed(my_list))
for i in range(0, (len(rev_list)), 2):
        rev_list[i] = rev_list[i] * (- 1)


final_list = rev_list + my_list
final_list.insert(num, 0)
print(f'"ЧУДЕСНАЯ" Негафибоначчи: {final_list}')


