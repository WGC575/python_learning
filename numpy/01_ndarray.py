import numpy as np
from numpy.lib import twodim_base

#declaration
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#object: array
#dtype: data type
#copy: copy needed or not
#order: C - row, F - column, A - either (default)
#subok: return an array whose type is the same as the base class
#ndmin: minimum dimension

simple_array = np.array([1, 2, 3])
two_dimension = np.array([[1, 2], [3, 4]])
minimum_dimension = np.array([1, 2, 3, 4, 5])
complex = np.array([1, 2, 3], dtype = complex)

print(simple_array, '\n', two_dimension, '\n', minimum_dimension, '\n', complex, '\n')
