"""
Problem:
Given an array of integers nums, return the frequency
of every distinct element.

Return the result as a list of [element, frequency] pairs.
"""

def countFrequencies(nums):
    freq={}
    for x in nums:
        freq[x]=freq.get(x,0)+1
        
    res=[]
    for key in freq:
        res.append([key,freq[key]])     # stores the val along with its frequence
    return res

print(countFrequencies([1,2,2,1,3]))


# T.C: O(N)
# S.C: O(k)
# k = number of unique elements