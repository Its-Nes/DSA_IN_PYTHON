# Pattern 1 - Square Star Pattern
"""
Problem:
Given an integer n, print a square pattern of '*' consisting
of n rows and n columns.
"""

def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
    print()     # blank line after each test case


# Driver code
t=int(input("No. of testcases: "))      # 3
n=list(map(int, input().split()))       # 1 2 3
for i in range(t):
    square(n[i])


# t.c: O(n^2) per test case
# s.c: O(1)