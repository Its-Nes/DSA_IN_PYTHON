# Step 1 - Python Basics

This folder contains the fundamental Python concepts required for solving Data Structures and Algorithms problems.

---

# Topics Covered

- Variables
- Input / Output
- Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- List Comprehensions
- Built-in Functions
- Math Functions
- Exception Handling

---

# Variables

```python
x = 10          #int
name = "Nes"    #string
pi = 3.14       #float
flag = True     #Boolean
```

---

# Input

```python
n = int(input())

s = input()

a, b = map(int, input().split())

arr = list(map(int, input().split()))
```

---

# Output

```python
print(x)

print(a, b)

print(*arr)

print("Answer =", ans)
```

---

# Data Types

```python
int
float
str
bool
list
tuple
set
dict
```

Check type

```python
type(x)
```

---

# Arithmetic Operators

```python
+
-
*
/
//
%
**
```

Example

```python
a = 10
b = 3

a + b
a - b
a * b
a / b   # 3/2 = 1.5 ;   -3/2 = -1.5
a // b  # integer division (floor division) 3//2 =1 ;   -3//2 = -2
a % b
a ** b
```

---

# Comparison Operators

```python
==
!=
<
>
<=
>=
```

---

# Logical Operators

```python
and
or
not
```

---

# If Else

```python
if x > 0:
    print("Positive")

elif x == 0:
    print("Zero")

else:
    print("Negative")
```

---

# Loops

## For Loop

```python
for i in range(5):
    print(i)
```

```python
for i in range(2, 10):
    print(i)
```

```python
for i in range(10, 0, -1):      #start,stop,step
    print(i)
```

---

## While Loop

```python
while n > 0:
    print(n)
    n -= 1
```

---

# Functions

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

---

# Strings

```python
s = "python"
```

Length

```python
len(s)
```

Indexing

```python
s[0]

s[-1]
```

Slicing

```python
s[1:4]

s[::-1]
```

Common Methods

```python
s.lower()

s.upper()

s.strip()

s.split()

" ".join(list)

s.replace("a", "b")

s.count("a")

s.find("a")
```

---

# Lists

Create

```python
arr = [1,2,3]
```

Access

```python
arr[0]

arr[-1]
```

Methods

```python
append()

extend()

insert()

remove()

pop()

clear()

sort()

reverse()

count()

index()
```

Loop

```python
for x in arr:
    print(x)
```

---

# Tuples

```python
t = (1,2,3)
```

Immutable

```python
t[0]
```

---

# Sets

```python
s = {1,2,3}
```

Methods

```python
add()

remove()

discard()

pop()

clear()
```

Operations

```python
a | b

a & b

a - b

a ^ b
```

---

# Dictionaries

Create

```python
d = {
    "a":1,
    "b":2
}
```

Access

```python
d["a"]

d.get("a")
```

Methods

```python
keys()

values()

items()

update()

pop()

clear()
```

Loop

```python
for key, value in d.items():
    print(key, value)
```

---

# List Comprehension

```python
arr = [i for i in range(10)]

arr = [i*i for i in range(10)]

even = [i for i in range(20) if i % 2 == 0]
```

---

# Enumerate

```python
for idx, value in enumerate(arr):
    print(idx, value)
```

```python
arr = ["A", "B", "C"]

for i, val in enumerate(arr, start=1):
    print(i, val)
```
Output

    1 A
    2 B
    3 C

---

# Zip

```python
a = [1,2,3]
b = [4,5,6]

for x, y in zip(a, b):
    print(x, y)
```
Output

    1 4
    2 5
    3 6

### Different lengths
```python
a = [1,2,3]
b = [4,5]

for x, y in zip(a, b):
    print(x, y)
```
Output

    1 4
    2 5

zip() stops when the shortest iterable ends.

---

# Lambda

```python
square = lambda x: x*x

print(square(5))
```

Examples
```python
#Add two numbers
add = lambda a, b: a+b

print(add(3,5))
```
Output: 8

```python
#Check even
even = lambda x: x%2==0

print(even(8))
```
Output: True



## Sorting
Suppose you have
```python
arr = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]
```
By default, arr.sort() sorts by the first element of each tuple.

    ("Alice",90)
    ("Bob",75)
    ("Charlie",85)

because "Alice", "Bob", "Charlie" come first.

### Sort by marks
```python
arr.sort(key=lambda x: x[1])
```
Output

    [
    ('Bob',75),
    ('Charlie',85),
    ('Alice',90)
    ]


---

# Useful Built-in Functions

```python
len()

max()

min()

sum()

sorted()

reversed()

abs()

round()

pow()

range()

enumerate()

zip()

map()

filter()

any()

all()
```

---

# Math Module

```python
import math
```

```python
math.sqrt()

math.ceil()

math.floor()

math.factorial()

math.gcd()

math.lcm()

math.log()

math.sin()

math.cos()

math.pi
```

---

# Exception Handling

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Time Complexity Reminder

| Operation | Complexity |
|-----------|------------|
| List Append | O(1) |
| List Pop End | O(1) |
| List Insert Beginning | O(n) |
| Search in List | O(n) |
| Dictionary Lookup | O(1) |
| Set Lookup | O(1) |
| Sorting | O(n log n) |

---

# Folder Contents
- Syntax
- Basic Mathematics
- Patterns
- Hashing
- Recursion

---

### Author: *[Its-Nes](https://github.com/Its-Nes)*

---
    If you find this repository useful
    Feel free to star the repository!

    Happy Coding! 🚀