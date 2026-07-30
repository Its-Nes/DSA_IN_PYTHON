# Pattern 10 - Repeated Number Triangle
"""
Problem:
Given an integer n, print a right-angled triangle
where each row contains the row number repeated.

Example:
Input:
n = 4

Output:
1
2 2
3 3 3
4 4 4 4
"""

def repeated_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

    print()     # Blank line after each test case


# Driver Code
t = int(input("No. of testcases: "))
nums = list(map(int, input().split()))
for i in range(t):
    repeated_number_triangle(nums[i])

# T.C: O(n²)
# S.C: O(1)