__author__ = 'vaishali'
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = map(int,raw_input().split(" "))
first, second = None, None
for n in A:
    if n > first:
        first, second = n, first
    elif first > n > second:
        second = n
print second

#def second_largest(numbers):
