# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from curses.ascii import isdigit


with open(r'D:\Learning\WorkFolder\py.basic\homework\HW4\1st_poli.txt', 'r') as f_1:
    string_1 = f_1.readline()

string_1 = string_1.split(' ')
string_1 = list(map(str, string_1))

with open(r'D:\Learning\WorkFolder\py.basic\homework\HW4\2nd_poli.txt', 'r') as f_2:
    string_2 = f_2.readline()

string_2 = string_2.split(' ')
string_2 = list(map(str, string_2))

print(string_1)
print(string_2)


# def poli_math (lst):
#     for item in range(len(lst)):
#         for i in lst[item]:
#             if item[i] == 'x':  # мысли закончилисб :^(

