__author__ = 'vaishali'
"""
Exceptions

Errors detected during execution are called exceptions.

Examples:

ZeroDivisionError
Raised when the second argument of a division or modulo operation is zero.

>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero

ValueError
Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
Handling Exceptions

try and except statements can be used to handle selected exceptions. A try statement may have more than one except clause, to specify handlers for different exceptions.

#Code
try:
    print 1/0
except ZeroDivisionError as e:
print "Error Code:",e

#Output
Error Code: integer division or modulo by zero
Task

You are given two values a and b.
Your task is to do integer division and print a/b.

Input Format

First line contains, number of testcases T.
Next T line contains, space separated values of a and b.

Constraints

0<T<10

Output Format

Print value of a/b.
In case of ZeroDivisionError or ValueError, print the error code.
"""
for i in range(int(raw_input())):
    try:
        a,b = map(int, raw_input().split())
        print a/b
    except ZeroDivisionError as e:
        print 'Error Code:',e
    except ValueError as e:
        print 'Error Code:',e