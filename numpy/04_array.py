import numpy as np

#array with 0s
x = np.empty([3, 2], dtype = int)
print(x)

#numpy.zeros(shape, dtype = float, order = 'C')
#fill the array with 0s

x = np.zeros((5,), dtype = np.int)
print(x)

x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)

#numpy.ones(shape, dtype = None, order = 'C')
#fill the array with 1s