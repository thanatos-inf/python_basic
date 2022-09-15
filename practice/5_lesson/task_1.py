# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

# with open(r'D:\Learning\WorkFolder\py.basic\practice\5_lesson\text.txt', 'r') as f:



# def find_missing(my_list):
#     for i in range(0, len(my_list) -1):
#         if (my_list[i + 1] - my_list[i]) > 1:
#             return my_list[i] + 1



with open(r'D:\Learning\WorkFolder\py.basic\practice\5_lesson\text.txt', 'r') as f:
    string = f.readline()

string = string.split(' ')
string = list(map(int, string))

# for i in range(1, len(string)):
#     if string[i] - 1 != string[i - 1]:
#         print(f'Missed: {string[i] - 1}')
#         break
# else:
#     print('Goog')

# 2 Вариант
lst = [(string[i] - 1) for i in range(1, len(string)) if string[i] - 1 != string[i - 1]]
print(lst)