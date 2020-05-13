t1,t2,n=map(int,input().split())
array=[0 for _ in range(n)]
array[0]=t1
array[1]=t2
for i in range(2,n):
    array[i]=array[i-2]+(array[i-1]*array[i-1])
print(array[n-1])
