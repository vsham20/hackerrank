__author__ = 'vaishali'
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,k = raw_input().split(" ")
for e in list(permutations(sorted(S),int(k))):
    print "".join(e)

