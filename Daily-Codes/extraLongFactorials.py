n=int(input())
array=[1 for _ in range(n+1)]
for i in range(1,n+1):
    array[i]=array[i-1]*i
print(array[n])
