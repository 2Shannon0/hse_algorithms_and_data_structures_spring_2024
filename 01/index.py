#СОРТИРОВКА
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[0] < pivot[0]]
    middle = [x for x in arr if x[0] == pivot[0]]
    right = [x for x in arr if x[0] > pivot[0]]
    
    return quicksort(left) + middle + quicksort(right)

#ЧТЕНИЕ ФАЙЛА
def read_file_to_array(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                key, value = parts
                result.append((int(key), value))
    return result
