__author__ = 'vaishali'
from collections import Counter
X = input()
S = Counter(map(int,raw_input().split()))
N = input()
earnings = 0
for customer in range(N):
    size, x_i = map(int,raw_input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i

print earnings 