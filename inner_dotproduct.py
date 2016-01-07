__author__ = 'vaishali'
import numpy
A = numpy.array([map(int,raw_input().split())])
B = numpy.array([map(int,raw_input().split())])
t = numpy.inner(A,B)
print t[0][0]
print numpy.outer(A,B)