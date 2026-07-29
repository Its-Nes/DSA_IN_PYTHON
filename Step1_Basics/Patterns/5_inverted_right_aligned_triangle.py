# Pattern 6 - Inverted Right-Aligned Triangle
"""
Problem:
Given an integer n, print an inverted right-aligned
triangle consisting of '*' characters.

Example:
Input:
n = 4

Output:
* * * *
  * * *
    * *
      *
"""

def inverted_right_aligned_triangle(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)

    print()     # Blank line after each test case


# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    inverted_right_aligned_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)