# Функция sum_list вычисляет сумму элементов списка lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] # определение списка

def sum_lst(lst):

    if not lst: # Если lst пуст, то функция возвращает 0 (базовый случай)
        return 0
    # Иначе, функция возвращает сумму первого элемента lst[0] и результата вызова sum_list для оставшейся части списка lst[1:]
    return lst[0] + sum_lst(lst[1:])

print(sum_lst(lst)) # вывод результата