def countFrequencies(nums):
    freq={}
    for x in nums:
        freq[x]=freq.get(x,0)+1
        
    res=[]
    for key in freq:
        res.append([key,freq[key]])
    return res

print(countFrequencies([1,2,2,1,3]))