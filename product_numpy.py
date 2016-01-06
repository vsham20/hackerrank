__author__ = 'vaishali'
import numpy
N, M = map(int, raw_input().split())
A =  numpy.array([map(int, raw_input().split()) for i in range(N)])
B = numpy.sum(A, axis = 0)
print numpy.prod(B)