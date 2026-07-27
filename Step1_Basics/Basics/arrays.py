# Take an integer n, 
# then store n elements in an array, and print them.

n=int(input("Enter size: "))
arr=list(map(int, input().split()))

#print(*arr)
for i in range(n):
    print(arr[i], end=" ")
print()

print("Reverse:", *arr[::-1])
