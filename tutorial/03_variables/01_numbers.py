from math import ceil, floor, sqrt, sin, cos, tan, tanh, pi
from random import random, randrange


x = 1   #int
print("x = 1")
y = 1.1 #float
print("y = 1.1")
z = 1j  #complex
print("z = 1j")
print()

#binary
num = 11
print("turn 11 to binary: "'{0:b}'.format(num))
b = f'{num:b}'
print("use f'{num:b}' also works: ", b)
# turning it to a string (binary form). This doesn't mean the variable is a binary one.
print("here, the type of b is: ", type(b))
print()

#use type() to verify the variable type
print("x:", type(x))
print("y:", type(y))
print("z:", type(z))
print()

# abs, ceil and floor
x = -1.1
print("x = -1.1")
print("abs(x):", abs(x))
print("ceil(x):", ceil(x))
print("floor(x):", floor(x))
print()

# largest and smallest number in a set/group of numbers
set_1 = set((1, 2, 3))
print("set_1 = set((1, 2, 3))")
print("max:", max(set_1))
print("min:", min(set_1))
print()

# sqare root and power
print("sqrt(1.44):", sqrt(1.44))
print("pow(5, 3), 5^3:", pow(5, 3))
print()

# random number, from random package. Note: there are different available random functions 
print("A random number from random():", random())
print()

# random range, randrange(start, stop, step). This is also from random package
print("return a number in a range with certain step by randrange(1, 5, 1):", randrange(1, 5, 1))

# trigonometric functions, others, not listed, include acos, asin, etc.
print("sin(30 degree):", sin(pi/6)) 
print("cos(30 degree):", cos(pi/6))
print("tan(30 degree):", tan(pi/6))
print("tanh(30 degree):", tanh(pi/6))
print()

# formatting floating numbers {:xxx.xxxf}.format(number) <- this is only a very brief intro to formatting
print("formatting numbers:")
print("sin(30 degree):", '{:.2f}'.format(sin(pi/6))) 
print("cos(30 degree):", '{:10.2f}'.format(cos(pi/6)))
print("tan(30 degree):", '{:010.2f}'.format(tan(pi/6)))
print("tanh(30 degree):", '{:.2f}'.format(tanh(pi/6)))



