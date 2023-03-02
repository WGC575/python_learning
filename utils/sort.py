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
    if len(arr) < 1:
        return arr
    
    # sort halves recursively
    mid = len(arr) // 2 # floor
    left_half = arr[:mid]
    right_half = arr[mid:]
