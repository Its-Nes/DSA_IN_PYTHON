# Pattern 2 - Right-Angled Triangle
"""
Problem:
Given an integer n, print a right-angled triangle
consisting of '*' characters.

Example:
Input:
n = 4

Output:
*
* *
* * *
* * * *
"""

def triangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()
    print()         # blank line after each test case

# Driver code
t=int(input("No. of testcases: "))      # 3
n=list(map(int, input().split()))       # 1 2 3
for i in range(t):
    triangle(n[i])


# t.c: O(n^2) per test case
# s.c: O(1)