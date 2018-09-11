import pandas

import numpy

myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['a','b']
colnames = ['one','two','three']
mydataframe = pandas.DataFrame(myarray,index=rownames,columns=colnames)
print(mydataframe)