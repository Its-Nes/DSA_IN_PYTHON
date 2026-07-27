n=int(input("Enter n: "))
for i in range(n):
    print(i+1, end=" ")


'''
Common patterns 

-> 0 to n-1
for i in range(n):
--------------------

-> 1 to n
for i in range(1, n+1):
--------------------

-> reverse n to 1
for i in range(n, 0, -1):       # start, stop, step
---------------------

-> skip values (step = 2)
for i in range(1, n+1, 2):
'''