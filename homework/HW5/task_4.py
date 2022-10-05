# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data): 
    encoded_data = '' 
    previous_symbol = '' 
    count = 1 
    
    if not data: return '' 
    
    for symbol in data:
        if symbol != previous_symbol:
            if previous_symbol:
                encoded_data += str(count) + previous_symbol
            count = 1
            previous_symbol = symbol
        else:
            count += 1
    else:
        encoded_data += str(count) + previous_symbol
        return encoded_data


def rle_decode(data):
    decoded_data = ''
    count = ''
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else:
            decoded_data += symbol * int(count)
            count = ''
    return decoded_data

with open(r'D:\Learning\WorkFolder\py.basic\homework\HW5\input.txt', 'r') as data_in:
    input_data = data_in.read()

new_encoded_data = rle_encode(input_data)    
print(new_encoded_data)

with open(r'D:\Learning\WorkFolder\py.basic\homework\HW5\output.txt', 'w') as data_out:
    input_data = data_out.write(rle_decode(new_encoded_data))

print(rle_decode(new_encoded_data))

