m,n=map(int,input().split())
a=list(map(int,input().split()))
arr=[0 for _ in range(m+1)]
arr[0]=1
for i in a:
    k=i
    while(k<m+1):
        arr[k] += arr[k-i]
        k += 1
print(arr[-1]) 
