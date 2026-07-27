# Pass by value(Immutable) - int, float, string, tuple

def change(x):
    x=10
    print("Inside function:", x)
a=5
change(a)
print("Outside function:",a)

#------------------------------------------------------
#Pass by reference(Mutable) - list, dictionary, set

def change2(arr):
    arr.append(4)
    print("Inside function:", arr)

l=[1,2,3]
change2(l)
print("Outisde function:",l)