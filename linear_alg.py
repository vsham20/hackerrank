__author__ = 'vaishali'

import numpy
N = int(raw_input())
A = numpy.array([map(float,raw_input().split()) for i in range(0,N)])
print numpy.linalg.det(A)