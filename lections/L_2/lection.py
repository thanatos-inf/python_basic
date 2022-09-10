# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет 
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close() # остановка программы


#--- Другой вариант записи ---
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit() # команда для того, чтобы не активировать всё, что записано после неё


#--- ФУНКЦИИ ---

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5))

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string(5))

# def concatenatio(*params):   # * перед наименованием переменной позволяет принимать любое их кол-во
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('d', 's', 'w'))
# print(concatenatio('1', 's', 'w', '3', '6'))

#--- РЕКУРСИЯ ---

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 11):
#     list.append(fib(e))

# print(list)

#---КОРТЕЖИ---

# a = (3, 1, 41, 4) # в данном случае кортеж = неизменяемый список. Присвоить элементам другие значения по ходу - НЕЛЬЗЯ
# print(a)
# print(a[-2])
# b = (3, )  # одиночный кортеж

# a = (3, 4, 5)
# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {} g: {} b: {}'.format(red, green, blue))


#---СЛОВАРИ---

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }

# # обратный слэш нужен, чтобы не записывать все значения словаря в одну строку

# for v in dictionary:
#     print(dictionary[v])

#---МНОЖЕСТВА---

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' - ошибка в случае удаления элемента, которого нет в множестве
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

#---СПИСКИ---

list1 = [1, 2, 3, 4, 5]
print(list1)
# print(list1.pop())  # удаление последнего элемента в списке
# print(list1)
# print(list1.pop(2)) # удаление элемента с конкретным индексом
# print(list1)
print(list1.insert(2, 11)) # добавление элемента на конкретную позицию
print(list1)
# print(list1.append(11)) # добавление элемента в конец
# print(list1)