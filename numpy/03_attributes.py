import numpy as np

"""
https://www.runoob.com/numpy/numpy-array-attributes.html
属性	说明
ndarray.ndim	秩，即轴的数量或维度的数量
ndarray.shape	数组的维度，对于矩阵，n 行 m 列
ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype	ndarray 对象的元素类型
ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
ndarray.flags	ndarray 对象的内存信息
ndarray.real	ndarray元素的实部
ndarray.imag	ndarray 元素的虚部
ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
"""

#0~23, 1 dimension
a = np.arange(24)
print(a)
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

print(a.ndim)
#1

b = a.reshape(2, 4, 3)
print(b)

print(b.ndim)
#3

a = np.array([[1, 2, 3],[4, 5, 6]])
print(a.shape)
#(2, 3), row, column

b = a.reshape(3,2) #doesn't change a directly but return a reshaped array
print(b)
#[[1, 2],
# [3, 4]
# [5, 6]]

x = np.array([1, 2, 3, 4, 5])
print(x.flags)




