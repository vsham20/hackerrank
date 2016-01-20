__author__ = 'vaishali'
"""
You are given data in a tabular format. The data contains N rows, and each row contains M space separated elements.

You can imagine the M items to be different attributes, (like height, weight, energy, etc.) and each of the N rows as an instance or a sample.

Your task is to sort the table on the Kth attribute and print the final resulting table.

Note: If two attributes are the same for different rows, print the row that appeared first in the input.

Input Format

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Constraints

1?N,M?1000
0?K<M
Each element ?1000

Output Format

Print the N lines of the sorted table. Each line should contain the space separated elements.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = raw_input().split()
list = []
for i in range(int(N)):
    list.append(map(int,raw_input().split()))
K = int(raw_input())
for i in sorted(list, key = lambda x:x[K]):
    str1 = ' '.join(str(e) for e in i)
    print str1