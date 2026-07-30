# Pattern 9 - Number Triangle
"""
Problem:
Given an integer n, print a right-angled triangle
where each row contains numbers from 1 up to the row number.

Example:
Input:
n = 4

Output:
1
1 2
1 2 3
1 2 3 4
"""

def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print()     # Blank line after each test case


# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))

for i in range(t):
    number_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)
