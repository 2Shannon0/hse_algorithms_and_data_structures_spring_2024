# ЧТЕНИЕ ФАЙЛА
def read_file_to_take_arguments(file):
    text = ""
    pattern = ""
    with open(file, "r") as file1:
        pattern = file1.readline()[:-1].lower()
        for line in file1:
            text += line.lower()
    return text, pattern


# Определение номеров строк и слов
def calculate_line_and_word_numbers(txt, s):
    line_number = 1
    word_number = 1

    # необходимо для кореектной обработки двойного пробела
    in_word = False

    for i in range(s):
        if txt[i] == "\n":
            line_number += 1
            word_number = 1
            in_word = False
        elif txt[i] == " ":
            if in_word:
                word_number += 1
            in_word = False
        else:
            in_word = True

    return line_number, word_number


# Алгоритм Бойера-Мура
NO_OF_CHARS = 256


def badCharHeuristic(string):
    badChar = [-1] * NO_OF_CHARS
    for i in range(len(string)):
        badChar[ord(string[i])] = i
    return badChar


def b_m_search(txt, pat):
    result = []
    m = len(pat)
    n = len(txt)

    if n == m == 0:
        return result

    badChar = badCharHeuristic(pat)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and (pat[j] == txt[s + j] or txt[s + j] == "\n"):
            j -= 1
        if j < 0:
            line_number, word_number = calculate_line_and_word_numbers(txt, s)
            # print("Шаблон найден при сдвиге = {}, Cтрока = {}, Cлово = {}".format(s, line_number, word_number))
            result.append(f"{line_number}, {word_number}")
            s += m - badChar[ord(txt[s + m])] if s + m < n else 1
        else:
            s += max(1, j - badChar[ord(txt[s + j])])
    return result


# Запись результов в файл (для тестов)
def write_result_in_file(input_path, output_path):
    text, pattern = read_file_to_take_arguments(input_path)
    result = b_m_search(text, pattern)
    if output_path is not None:
        with open(output_path, "w") as file:
            for el in result:
                file.write(f"{el}\n")
