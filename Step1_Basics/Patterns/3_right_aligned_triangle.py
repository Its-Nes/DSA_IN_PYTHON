# Pattern 3 - Right-Aligned Triangle
"""
Problem:
Given an integer n, print a right-aligned triangle
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

def right_aligned_triangle(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)

    print()     # Blank line after each test case


# Driver code
t = int(input("No. of testcases: "))        # 2
nums = list(map(int, input().split()))      # 2 3
for i in range(t):
    right_aligned_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)


#--------------------------------------

# If you don't want spaces between stars:
# print(" " * (n - i) + "*" * i)

# If you want spaces between stars (better alignment):
# print("  " * (n - i) + "* " * i)