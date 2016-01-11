__author__ = 'vaishali'
"""
cmath.phase
This tool returns the phase of complex number z (also known as the argument of z).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

abs
This tool returns the modulus (absolute value) of complex number z.

>>> abs(complex(-1.0, 0.0))
1.0

Task
You are given a complex z. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number z.

Output Format

Output two lines:
The first line should contain the value of r.
The second line should contain the value of ?.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import *
a = polar(complex(raw_input())) # polar() converts complex number into polar
print a[0]
print a[1]