# What is Hashing (simple words)

Hashing = storing data in a way that lets you find it instantly

Instead of searching through a list again and again,
you use a hash table (in Python → dictionary) to get answers in O(1) time.

---

# 🔑 Real intuition

Imagine this:

You ask:
👉 “How many times does 3 appear?”

Without hashing:
You scan the whole array every time 😓 → O(n)

With hashing
You already stored:

3 → 4 times
So you answer instantly 😌

---

# Hashing in Python = Dictionary
```
freq = {}
arr = [1, 2, 1, 3, 2, 1]

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
```
Output
{1: 3, 2: 2, 3: 1}

### Shortcut (cleaner way)
```
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
```
---

# 📌 Most important use cases
## 1️⃣ Frequency Count
arr = [1,1,2,3,3,3]


→ count occurrences

## 2️⃣ Check if element exists
```
if x in freq:
    print("Found")
```
## 3️⃣ Find duplicates
```
if freq[num] > 1:
    print(num)
```
## 4️⃣ Character hashing (strings)
```
s = "aabbc"

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output:
{'a': 2, 'b': 2, 'c': 1}

---

## ⚡ Why hashing is powerful
    Operation	Time
    Search	    O(1)
    Insert	    O(1)
    Delete	    O(1)

Compare that with arrays:
→ O(n) 

### Common mistake beginners make:

Using nested loops

    for i in arr:
        for j in arr:


👉 Instead → use hashing → O(n)

💡 One-line summary:

    Hashing = store once, answer instantly.