__author__ = 'vaishali'
import numpy
N,M = map(int,raw_input().split())
A = numpy.array([map(int,raw_input().split()) for i in range(0,N)])
print numpy.mean(A, axis = 1)
print numpy.var(A , axis = 0)
print numpy.std(A , axis = None)
