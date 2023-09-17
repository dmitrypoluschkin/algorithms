def binary_search_recursive(arr, target):

    if not arr:
        return False
    
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        return binary_search_recursive(arr[:mid], target)
    else:
        return binary_search_recursive(arr[mid + 1:], target)
    


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_number = 6
result = binary_search_recursive(sorted_list, target_number)
print(f"Число {target_number} {'найдено' if result else 'не найдено'} в списке.")

