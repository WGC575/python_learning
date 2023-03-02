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

arr = [5, 2, 8, 3, 1, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)