# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя.   
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# def seq(list):
#     for i in range():


my_list = [1, 5, 2, 3, 4, 6, 1, 7]
count = 0 
new_list = ([my_list[i] for i in range(1,len(my_list)) if my_list[i] >= max(my_list[0:i])])
new_list.insert(0, my_list[0])
print(new_list)
