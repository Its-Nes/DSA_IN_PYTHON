# Pattern 4 - Inverted Right-Angled Triangle
"""
Problem:
Given an integer n, print an inverted right-angled triangle
consisting of '*' characters.

Example:
Input:
n = 4

Output:
* * * *
* * *
* *
*
"""

def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

    print()     # Blank line after each test case


# Driver Code
t = int(input("No. of testcases: "))        # 2
nums = list(map(int, input().split()))      # 3 4
for i in range(t):
    inverted_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)
