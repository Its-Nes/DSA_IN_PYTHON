# Recursion in Python

Recursion is a programming technique in which a function calls itself to solve a problem by breaking it down into smaller subproblems.

Instead of solving the entire problem at once, recursion solves one smaller instance of the same problem until a **base case** is reached.

---

# Structure of a Recursive Function

Every recursive function must have two parts:

1. **Base Case**
   - The stopping condition.
   - Prevents infinite recursive calls.

2. **Recursive Case**
   - The function calls itself with a smaller input.

```python
def recursion():
    if base_case:
        return

    recursion(smaller_input)
```

---

# How Recursion Works

Suppose we call:

```python
print_numbers(3)
```

```python
def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n-1)
```

Execution:

```
print_numbers(3)
|
|-- print(3)
|
|-- print_numbers(2)
      |
      |-- print(2)
      |
      |-- print_numbers(1)
             |
             |-- print(1)
             |
             |-- print_numbers(0)
                    |
                    |-- return
```

Output

```
3
2
1
```

---

# Recursion Tree

Example:

```python
fib(4)
```

```
                fib(4)
              /        \
         fib(3)       fib(2)
        /     \       /     \
    fib(2) fib(1) fib(1) fib(0)
    /   \
fib(1) fib(0)
```

A recursion tree helps visualize recursive calls.

---

# Call Stack

Recursive function calls are stored inside the **Call Stack**.

Example:

```python
func(3)
```

Stack:

```
func(3)
func(2)
func(1)
func(0)
```

Once the base case is reached, functions return one by one.

```
func(0) returns
func(1) returns
func(2) returns
func(3) returns
```

This is called **Backtracking**.

---

# Base Case

The base case is the condition that stops recursion.

Without a base case:

```python
def func():
    func()
```

This causes

```
RecursionError:
maximum recursion depth exceeded
```

---

# Recursive Case

The recursive case should always move towards the base case.

Example:

```python
func(n-1)
```

If the problem size never decreases, recursion never ends.

---

# Types of Recursion

## 1. Linear Recursion

Only one recursive call is made.

```python
func(n-1)
```

Example

- Factorial
- Sum of N numbers

---

## 2. Binary Recursion

Each function makes two recursive calls.

```python
func(n-1)
func(n-2)
```

Example

- Fibonacci

---

## 3. Multiple Recursion

More than two recursive calls.

Example

- Tree Traversals
- N-Queens
- Backtracking

---

## 4. Tail Recursion

Recursive call is the last statement.

```python
def func(n):
    if n==0:
        return

    func(n-1)
```

No work remains after the recursive call.

---

## 5. Head Recursion

Recursive call happens before processing.

```python
def func(n):
    if n==0:
        return

    func(n-1)
    print(n)
```

Output

```
1
2
3
```

---

# Dry Run

Example

```python
factorial(4)
```

```
factorial(4)

=4 × factorial(3)

=4 × 3 × factorial(2)

=4 × 3 × 2 × factorial(1)

=4 × 3 × 2 × 1

=24
```

---

# Advantages

- Clean and readable code
- Natural solution for recursive problems
- Useful for trees and graphs
- Simplifies divide-and-conquer algorithms
- Makes backtracking easier

---

# Disadvantages

- Extra memory due to call stack
- Slower than iteration
- Stack overflow for deep recursion
- Sometimes difficult to debug

---

# Recursion vs Iteration

| Recursion | Iteration |
|-----------|-----------|
| Uses function calls | Uses loops |
| Uses call stack | No call stack |
| Easier for recursive problems | Usually faster |
| More memory | Less memory |
| Elegant code | Efficient code |

---

# Time Complexity

Depends on the number of recursive calls.

Examples

| Problem | Time Complexity |
|----------|----------------|
| Print N numbers | O(N) |
| Factorial | O(N) |
| Sum of N numbers | O(N) |
| Reverse Array | O(N) |
| Fibonacci (recursive) | O(2^N) |
| Binary Search | O(log N) |
| Merge Sort | O(N log N) |

---

# Space Complexity

Space Complexity = Recursion Stack Depth

Examples

| Problem | Space Complexity |
|----------|-----------------|
| Print N numbers | O(N) |
| Factorial | O(N) |
| Reverse Array | O(N) |
| Fibonacci | O(N) |
| Binary Search | O(log N) |

---

# Common Recursive Problems

- Print 1 to N
- Print N to 1
- Sum of first N numbers
- Factorial
- Fibonacci
- Reverse an array
- Check palindrome
- Generate subsequences
- Generate subsets
- Combination Sum
- N Queens
- Sudoku Solver
- Rat in a Maze
- Tower of Hanoi
- Merge Sort
- Quick Sort
- Binary Search
- DFS on Trees
- DFS on Graphs

---

# When to Use Recursion

Use recursion when:

- The problem can be divided into smaller identical subproblems.
- The recursive solution is simpler than iteration.
- Working with trees or graphs.
- Solving divide-and-conquer algorithms.
- Implementing backtracking algorithms.

Avoid recursion when:

- Iteration provides a simpler solution.
- The recursion depth may become very large.
- Memory efficiency is important.

---

# Tips

- Always define a base case.
- Reduce the problem size in every recursive call.
- Think about the recursion tree.
- Dry run the call stack.
- If possible, convert repeated recursive work into Dynamic Programming.

---

# Problems Included

- Print Name N Times
- Print 1 to N
- Print N to 1
- Sum of First N Numbers
- Factorial
- Reverse Array
- Check Palindrome
- Fibonacci Number
- Tower of Hanoi
- Subsequences
- Subsequences with Sum K
- Combination Sum
- Merge Sort
- Quick Sort

---

Happy Coding! 🚀