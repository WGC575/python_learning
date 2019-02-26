#lambda function is a special function that calculate a certain expression (only one)
#with multiple parameters. It automatically returns the result of the expression.
x = lambda a, b: a + b
print(x(4,5))

#mixed use of normal functions and lambda function
#first define the function
def func(x):
    return lambda a: a + x
#in the second step, lambda is defined
add_2 = func(2)
print(add_2(5))
