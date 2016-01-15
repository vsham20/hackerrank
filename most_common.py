__author__ = 'vaishali'
"""
You are given a string  .
The string contains only lowercase alphabetic characters.

Your task is to find top three most common characters in the string  .

Input Format

Single line containing string  .

Constraints



Output Format

Print the most common characters along with their count of occurences in three lines.
Output must sorted in descending order of count of occurences.
If count of occurences is same then sort in ascending order of characters.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

S = raw_input()
counts = dict(Counter(S))
# sorting dictionary with their key in ascending order
rev_sort = sorted(counts.items(), key=lambda x: x[0])

# now sorting it with values in descending order
rev_sort = sorted(rev_sort, key=lambda x: x[1], reverse=True)



for i in range(3):
    print "{0} {1}".format(rev_sort[i][0], rev_sort[i][1])