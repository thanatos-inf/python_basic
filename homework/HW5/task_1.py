# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def clarify_text (text):
    input_list = text.split(' ')
    result = []
    odd_find = 'абв'
    for item in input_list:
        if odd_find not in item:
            result.append(item)
    return result

text = 'Неабв Надеюсь, абв что прокрастинабвция всё абвНЕ получится!'

print(*clarify_text(text))


# odd_find = 'абв'
# index = 0

# input_list = text.split(' ')
# print(input_list)

# result_list = [item for item in input_list if odd_find not in item]
# print(*result_list)

