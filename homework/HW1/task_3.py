# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = float(input('Введите координаты по оси Х: '))
y = float(input('Введите координаты по оси Y: '))

if (x > 0) and (y > 0):
    print('Точка находится в I квадранте.')
elif (x < 0) and (y > 0):
    print('Точка находится в II квадранте.')
elif (x < 0) and (y < 0):
    print('Точка находится в III квадранте.')
elif (x > 0) and (y < 0):
    print('Точка находится в IV квадранте.')
elif (x == 0) and ((y < 0) or (y > 0)):
    print('Точка находится на оси Y.')
elif ((x < 0) or (x > 0)) and (y == 0):
    print('Точка находится на оси Х.')
else:
    print('Точка находится в центре координатной плоскости.')
