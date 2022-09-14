# --- Немного Лямбды ---

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc(op, a, b):
#     print(op(a, b))

# calc(lambda x, y: x+y, 4, 5)

# --- List Comprehentions ---

# def f(x):
#     return x**3

# my_list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # для кортежей запись (i, i)
# print(my_list)

#--- Промежуточное задание

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input('Введите числа через пробел: ').split()))
# print(data)

# data = map(int, '1 2 3 66 55 87 9'.split())

# for e in data:
#     print(e)

#---Сводное решение
# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333] # функция zip уравнивает все данные по кратчайшему списку

data = list(zip(users, ids, salary))
data_2 = list(enumerate(users))
print(data)
print(data_2)