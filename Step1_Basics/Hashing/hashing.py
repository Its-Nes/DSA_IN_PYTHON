# Hashing is the process of precomputing and storing data
# in a data structure (list, dictionary, or set) so that
# future lookups become much fa

"""
Problem:
Given two arrays n and m, print the frequency of every element of m in n.

Constraints:
1 <= n[i] <= 10
"""

# ==========================================================
# Brute Force -- Nested Loops
# T.C: O(N*M)
# S.C: O(1)
# ==========================================================

def brute(n, m):        # Will result in TLE in worst case as 10^8 * 10^8 =10^16
    for num in m:
        c = 0
        for x in n:
            if x == num:
                c += 1
        print(c, end=" ")


# ==========================================================
# Better Solution (Hash Array / Hash List) 
# Optimal for the given constraints
# T.C: O(N+M)
# S.C: O(11) = O(1)
# ==========================================================

def optimal1(n, m):
    hash_list = [0] * 11        # As 1<=n[i]<=10, since python lists are 0-indexed to access idx 10 the list must have 11 elements, so from 0-11 (11th excluded)

    for x in n:                 # 0 1 2 3 4 5 6 7 8 9 10
        hash_list[x] += 1       # ------------------------
                                # 0 0 0 0 0 0 0 0 0 0  0
    for num in m:
        if 1 <= num <= 10:
            print(hash_list[num],end=" ")       
        else:
            print(0, end=" ")


# ==========================================================
# Optimal Solution (Dictionary Hashing)
# Preferred when the value range is unknown or large
# T.C: O(N+M)
# S.C: O(k)     k = no. of unique elements
# ==========================================================

def optimal2(n, m):
    freq = {}

    for x in n:
        freq[x] = freq.get(x, 0) + 1

    for num in m:
        print(freq.get(num, 0), end=" ")


# ==========================================================
# Driver Code
# ==========================================================

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

print("Brute Force:")
brute(n, m)

print("\n\nHash Array:")
optimal1(n, m)

print("\n\nDictionary:")
optimal2(n, m)


"""
Rule of thumb
 Known small range → Use a list (hash array).
 Unknown, large, or negative values → Use a dictionary.
"""