__author__ = 'vaishali'

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = raw_input().split()
M = raw_input().split()
A = raw_input().split()
B = raw_input().split()
count = 0
ding = 0
for i in M:
    for e in A:
        if i == e:
            count+= 1
    for f in B:
        if i == f:
            ding+= 1
happiness = count - ding
print happiness

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = raw_input().split()
M = raw_input().split()
A = raw_input().split()
B = raw_input().split()
count = 0
ding = 0
for i in M:
    for e in A:
        if i == e:
            count+= 1
    for f in B:
        if i == f:
            ding+= 1
happiness = count - ding
print happiness