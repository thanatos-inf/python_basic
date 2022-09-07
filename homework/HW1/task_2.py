
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input('Введите Х: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))


def is_true(x, y, z):
    left_part = not (x or y or z)
    right_part = not x and not y and not z
    result = left_part == right_part
    return result


if is_true(x, y, z) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")