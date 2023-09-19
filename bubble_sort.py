def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(arr))


# рекурсивная пузырьковая сортировка
def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    # Базовый случай: если длина списка равна 1, то он уже отсортирован
    if n == 1:
        return arr
    
    # Проходим по всем элементам списка
    for i in range(n-1):
        # Если текущий элемент больше следующего, меняем их местами
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # Рекурсивно вызываем функцию для уменьшенной длины списка
    return recursive_bubble_sort(arr, n-1)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = recursive_bubble_sort(arr)
print(sorted_arr)

    

