# ЧТЕНИЕ ФАЙЛА
def read_file_to_take_arguments(file):
    n = None
    m = None
    rectangle_by_strings = []
    with open(file, "r") as file1:
        n, m = file1.readline().split()
        for line in file1:
            if len(line) > 1:
                rectangle_by_strings.append(line[:-1])
            else:
                rectangle_by_strings.append(line)
    return int(n), int(m), rectangle_by_strings


def max_histogram_rectangle(hist):
    stack = []
    max_s = 0
    idx = 0

    while idx < len(hist):
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            height = hist[top]
            if len(stack) > 0:
                width = idx - stack[-1] - 1
            else:
                width = idx
            max_s = max(max_s, height * width)

    while stack:
        top = stack.pop()
        height = hist[top]
        if len(stack) > 0:
            width = idx - stack[-1] - 1
        else:
            width = idx
        max_s = max(max_s, height * width)

    return max_s


def max_rectangle_S_0(input_file):
    n, m, rectangle = read_file_to_take_arguments(input_file)
    print(rectangle)
    if n == m == 1:
        if rectangle[0] == "0":
            return 1
        else:
            return 0

    cur_hist = [0] * m
    max_s = 0
    for row in rectangle:
        for idx in range(m):
            if row[idx] == "0":
                cur_hist[idx] += 1
            else:
                cur_hist[idx] = 0
        max_s = max(max_histogram_rectangle(cur_hist), max_s)

    print(max_s)
    return max_s
