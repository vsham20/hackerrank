__author__ = 'vaishali'
"""
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import textwrap
S = str(raw_input())
w = int(raw_input())
print textwrap.fill(S ,w)