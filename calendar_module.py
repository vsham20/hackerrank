__author__ = 'vaishali'
"""
Task

You are given the date of the day. Your task is to find what day it is on that date.

Input Format

Single line containing space separated month, day and year in MM DD YYYY format.

Constraints

2000<year<3000

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015

Sample Output

WEDNESDAY

"""
import calendar

day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

m,d,y = map(int,raw_input().split())
print day[calendar.weekday(y,m,d)]