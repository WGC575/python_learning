#To find the second place in a array
n = 5
arr = [2, 3, 5, 6, 6]

first = -100
second = -100

for x in arr:
    if x > first:
        second = first
        first = x
    elif x < first and x > second:
        second  = x
print(second)