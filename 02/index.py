# ЧТЕНИЕ ФАЙЛА
def read_file_to_array(file):
    result = []
    with open(file, "r") as file1:
        for line in file1:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                key, value = parts
                save_key = key
                result.append((key, value, save_key))
    return result


# ВСПОМОГАТЕЛЬНАЯ СОРТИРОВКА ПОДСЧЕТОМ ДЛЯ ОДНОГО РАЗРЯДА
def counting_sort_digit(A, digit_index):
    if len(A) == 0:
        return
    out = [None] * len(A)
    k_max = max(line[0][digit_index] for line in A) + 1
    k_min = min(line[0][digit_index] for line in A)

    offset = 0
    if k_min < 0:
        offset = -k_min
    else:
        k_min = 0

    C = [0 for _ in range(k_min, k_max + 1)]
    for j in range(len(A)):
        C[A[j][0][digit_index] + offset] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for x in range(len(A) - 1, -1, -1):
        out[C[A[x][0][digit_index] + offset] - 1] = A[x]
        C[A[x][0][digit_index] + offset] -= 1
    return out


# ПАРСИНГ (ПРИВЕДЕНИЕ К НУЖНОМУ ФОРМАТА) ИСХОДНЫХ НОМЕРОВ
def parse_phone_number(phone_number):
    parts = phone_number.split("-")
    country_code = int(parts[0].replace("+", ""))
    city_code = int(parts[1])
    local_number = int("".join(parts[2:]))
    return country_code, city_code, local_number


# ПОРАЗРЯДНАЯ СОРТИРОВКА
def radix_sort(inputFilePath, outputFilePath):
    data = read_file_to_array(inputFilePath)
    if len(data) == 0:
        with open(outputFilePath, "w") as file:
            file.write("")
        return

    parsed_data = [
        (parse_phone_number(key), value, save_key) for key, value, save_key in data
    ]

    sorted_data = parsed_data

    for digit_index in reversed(range(3)):
        sorted_data = counting_sort_digit(sorted_data, digit_index)

    with open(outputFilePath, "w") as file:
        for _, value, save_key in sorted_data:
            file.write(f"{save_key}\t{value}\n")

    # for _, value, save_key in sorted_data:
    #     print(f'{save_key}\t{value}')

    return [(save_key, value) for _, value, save_key in sorted_data]
