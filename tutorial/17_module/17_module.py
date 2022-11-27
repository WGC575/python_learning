#use "from module import item" or "import module (as XXX)"
import numpy as np

#if in the same directory, the file could be easily imported with an import command
#if in other directory, the following command could be used
#import sys
#sys.path.append('D:/文档/个人_IT/python_learning')
#most filenames in this tutorial is begun with number which is not allowed for python code. 
#Although themselves work correctly, they could not be imported correctly
import utils.utils as ut

x = ut.Student("WGC575", "12")

#use "from" to import a part of the module

#use dir() to show the content of the package
x = dir(np)





