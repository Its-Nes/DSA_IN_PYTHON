# Pattern 8 - Diamond Pattern
"""
Problem:
Given an integer n, print a diamond pattern
consisting of '*' characters.

Example:
Input:
n = 4

Output:
      *
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
"""

def diamond(n):
    for i in range(n):      # Upper Pyramid
        print("  " * (n - i - 1) + "* " * (2 * i + 1))

    for i in range(1, n):   # Lower Inverted Pyramid
        print("  " * i + "* " * (2 * (n - i) - 1))

    print()


# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    diamond(nums[i])

# T.C: O(n²)
# S.C: O(1)