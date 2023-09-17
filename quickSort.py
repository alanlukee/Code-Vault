def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for element in arr[1:]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5, 2, 9, 3, 7, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)