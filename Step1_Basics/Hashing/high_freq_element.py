"""
Problem:
Given an array of integers nums, return the element that occurs
the maximum number of times (highest frequency).

If multiple elements have the same maximum frequency,
return the smallest among them.
"""

def mostFrequentElement(nums):
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
        
    max_freq=0
    ans=float('inf')

    for num, count in freq.items():
        if count > max_freq:
            max_freq = count
            ans = num

        elif count == max_freq:
            ans = min(ans, num)     # if 2 elements hv same freq
    return ans
        
print(mostFrequentElement([1,2,2,3,3,3]))


# t.c: O(n+k)  [for building freq dictionary and finding max freq element]
# s.c: O(k)  [k is no. of unique elements]