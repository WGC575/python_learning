#use def function(): to define a function and use function() to call it
def add(a, b):
    print(a + b)
add(1, 2)

#use return to return a result to the caller
def max(a, b):
    if a >= b:
        return a
    else:
        return b
x = max(3, 4)
print(x)