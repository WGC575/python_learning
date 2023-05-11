# 1. bubble sort

def bubble_sort(arr):
    n = len(arr)

    # traversal
    for i in range(n):
        # inner traversal
        for j in range(0, n-i-1):
            # swapping
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# example usage
#arr = [64, 34, 25, 12, 22, 11, 90]
#bubble_sort(arr)
#print("Sorted Array:", arr)

# 2. merge sort

def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    
    # sort halves recursively
    mid = len(arr) // 2 # floor
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # dealing with the last element
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(left_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

# example usage

#arr = [5, 2, 8, 3, 1, 6]
#sorted_arr = merge_sort(arr)
#print(sorted_arr)

# 3. quick sort

def quick_sort(arr, start = 0, end = None):
    if end is None:
        end = len(arr) - 1
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# example usage

arr = [5, 2, 8, 3, 1, 6]
sorted_arr = quick_sort(arr)
print(sorted_arr)