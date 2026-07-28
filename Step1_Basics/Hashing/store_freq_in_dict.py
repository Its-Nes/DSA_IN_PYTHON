"""
Problem:
Given an array of integers nums, count the frequency 
of each element and store the result in a dictionary.
"""

nums=list(map(int,input().split()))

freq={}
for i in nums:                  # O(N)     
    freq[i]=freq.get(i,0)+1     # O(1) in avg case
print(freq) 

# t.c: O(n)
# s.c: O(k)   k=no. of unique elements

#---------------------------------------
# For dictionaries we always consider avg case, 
# Accessing, updating, deleting, adding element all take O(1) time (in avg case)

# In the worst case, dictionary operations may take O(N)
# due to hash collisions, but this is extremely uncommon.
# Therefore, we consider them O(1) on average.

#---------------------------------------

# Another way
def storefreq(nums):
    freq={}
    for num in nums:             #->O(N)
        if nums[num] in freq:    #->O(1)
            freq[num]+=1         #->O(1)
        else:
            freq[num]=1          #->O(1)
    print(freq)   

storefreq(nums)

# T.C -> O(N)
# S.C -> O(k)   k= no. of unique elements. ( in worst case all are unique so we can write O(n))
