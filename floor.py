__author__ = 'vaishali'
import numpy

N= map(float, raw_input().split(" "))
A =  numpy.array(N)
print numpy.floor(A)
print numpy.ceil(A)
print numpy.rint(A)