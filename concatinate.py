__author__ = 'vaishali'
import numpy
N,M,P = raw_input().split(" ")
a = numpy.array( [map(int, raw_input().split()) for i in range(int(N))] )
b = numpy.array( [map(int, raw_input().split()) for i in range(int(M))] )
print numpy.concatenate((a,b), axis = 0)
