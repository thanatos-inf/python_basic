# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     *2) с помощью дополнительных библиотек Python

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    x = (-b) / 2 * a
    print(x)
else:
    x_1 = ((-b) + d ** 0.5) / 2 * a
    x_2 = ((-b) - d ** 0.5) / 2 * a
    print(x_1, x_2)

#---2 вариант---

# import sympy as sm

# from sympy.solvers import solve
# from sympy import Symbol


# def fun(a, b, c):
#     x = Symbol('x')
#     return solve(f'{a}*x**2+{b}*x+{c}', x)


# print('Корни уравнения:', *fun(1, -16, 28))  # 2 14
