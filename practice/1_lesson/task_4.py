# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую 
# цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

#Вариант 1 (python)
number = input("Input number: ")
print(number.split('.')[1][0])

#Вариант 2 (математика)
# number = float(input("Input number: "))
# number *= 10
# print(number)
# number = int(number)
# print(number)
# print(number % 10)

# // - Целая часть
# % - Остаток