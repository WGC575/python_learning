# Subarrays and references

# an array and simple references to elements
arr = [0, 1, 2, 3, 4]
print(arr[0])

# referencing a subarray: arr[left, right]
# NOTE: left included, right not
# left 3 elements
print(arr[0: 3])

# flooring the length to divide the array into left and right halves
# use [£º]
mid = len(arr) // 2

# NOTE: the floor is included in the right part
arr_left = arr[:mid]
arr_right = arr[mid:]
print(arr_left)
print(arr_right)
