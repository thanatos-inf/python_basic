# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Неабв Надеюсь, абв что прокрастинабвция всё абвНЕ получится!'

odd_find = 'абв'

input_string = text.split(' ')

result_list = [item for item in input_string if odd_find not in item]
print(*result_list)