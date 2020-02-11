# Fibonacci Series with DP approach

n=int(input("Enter the number of elements to be displayed\t"))
arr=[1 for _ in range(n)]
for i in range(2,n):
    arr[i]=arr[i-1]+arr[i-2]
for i in range(n):
    print(arr[i],end=" ")
