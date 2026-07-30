# Pattern 6 - Inverted Number Triangle
"""
Problem:
Given an integer n, print an inverted right-angled triangle
where each row contains numbers starting from 1.

Example:
Input:
n = 4

Output:
1 2 3 4
1 2 3
1 2
1
"""

def inverted_number_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print()     # Blank line after each test case


# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    inverted_number_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)