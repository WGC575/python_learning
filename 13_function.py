#use def function(): to define a function and use function() to call it
def add(a, b):
    return (a + b)

#add(1, 2)

def add(a, b, m):
    return ((a + b) * m)

#add(1, 2)

#use return to return a result to the caller
def max(a, b):
    if a >= b:
        return a
    else:
        return b

print(add(4, 4, 2))
print(add(4, 4))