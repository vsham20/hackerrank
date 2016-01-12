__author__ = 'vaishali'
"""
Problem Statement

Let's learn some new python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Input Format

An integer N

Output Format

A list containing cubes of first N fibonacci numbers.
"""
N = int(raw_input())
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

a = map(fibonacci, range(N))
print map((lambda x: x **3), a)