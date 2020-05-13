n,k=map(int,input().split())
arr=list(map(int,input().split()))
i=k
if k==0:
    print("100")
elif n==k:
    if arr[0]==0:
        print("99")
    else:
        print("97")
else:
    if arr[k]==1:
        count=3
    else:
        count=1
    while(i!=0):
        if arr[(i+k)%n]==1:
            count += 2
        count += 1
        i=(i+k)%n
    print(100-count)
