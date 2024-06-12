# ЧТЕНИЕ ФАЙЛА
def read_file_to_take_arguments(file):
    text = ''
    orders = []
    with open(file, "r") as file1:
        text = file1.readline()[:-1]
        for line in file1:
                orders.append(line[:-1]) #добавляем без символа переноса строки
    return text, orders


print(read_file_to_take_arguments('0-input.txt'))