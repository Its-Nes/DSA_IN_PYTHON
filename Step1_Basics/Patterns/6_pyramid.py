# Pattern 6 - Pyramid Pattern

"""
Problem:
Given an integer n, print a pyramid pattern
consisting of '*' characters.

Example:
Input:
n = 4

Output:
      *
    * * *
  * * * * *
* * * * * * *
"""

def pyramid(n):
    for i in range(n):
        print("  " * (n - i - 1) + "* " * (2 * i + 1))
    print()



# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    pyramid(nums[i])

# T.C: O(n²)
# S.C: O(1)