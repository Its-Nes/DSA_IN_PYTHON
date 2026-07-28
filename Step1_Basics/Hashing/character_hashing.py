"""
Problem:
Given a lowercase string s and a list q containing characters,
print the frequency of each character of q in string s.

Constraints:
'a' <= s[i] <= 'z'      (97-112)
"""

# calc freq of all ch in s, store in hash_list
# then answer each query in O(1)

s="azyuyyzaaaa"
q=['d','a','y','u']

hash_list=[0]*26        # we hv 26 alphabets (0 to 25=26)

for ch in s:
    idx=ord(ch)-97      # Used offset method (ASCII of 'a' = 97)
    hash_list[idx]+=1

for x in q:
    asciival=ord(x)
    idx=asciival-97
    print(hash_list[idx], end=" ")   

print()
# T.C -> O(N+M), N is len of string, and m is len of q
# S.C -> O(26) = O(1)

#-------------------------------------------
# Another way (dictionary hashing)
# efficient when string can contain any characters
# like letters, digits, symbols,spaces,unicode, etc. then we can use dictionary

s="azyuyyzaaaa"
q=['d','a','y','u']

freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1

for ch in q:
    print(freq.get(ch,0), end=" ")   

# T.C -> O(N+M)
# S.C -> O(k) ; k is unique characters in string

