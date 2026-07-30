# Pattern 7 - Inverted Pyramid
"""
Problem:
Given an integer n, print an inverted pyramid
consisting of '*' characters.

Example:
Input:
n = 4

Output:
*******
 *****
  ***
   *
"""

def inverted_pyramid(n):
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))

    print()

# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    inverted_pyramid(nums[i])


# T.C: O(n²)
# S.C: O(1)