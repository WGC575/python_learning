import numpy as np
import re

#data file name
filename = str("../datasets/4dim.train.txt")
#read data file, no comments
rawdata = np.loadtxt(filename, dtype = 'str', delimiter = '\t', comments = None, usecols = range(2))
#number of rows and columns
n_row = rawdata.shape[0]
n_column = rawdata.shape[1]
#print(n_row)
#print(n_column)

#data = np.loadtxt(rawdata, dtype = str, delimiter = '\t', usecols = range(2))
print(rawdata[2][1])