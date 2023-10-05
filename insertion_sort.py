def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

my_list = [23, 45, 87, 56, 37, 39, 84, 33, 90, 32, 7]

sort_my_list = insertion_sort(my_list)
print(sort_my_list)