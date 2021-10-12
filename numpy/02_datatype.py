import numpy as np

#numpy data object: numpy.dtype(object, alogn, copy)
#object: data object
#align, true for c-like struct
# int8, int16, int32, int64 <- 'i1', 'i2','i4','i8' 

n = np.dtype(np.int32)
n= np.dtype('i4')
#int32


n_structure = np.dtype([('age', np.int8)])
#[('age', 'i1')]

n_ndarray = np.dtype([('age', np.int8)])
a = np.array([()])
