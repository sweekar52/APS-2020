t=int(input())
for _ in range(t):
    count=0
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]<1:
            count += 1
    if count>=k:
        print("NO")
    else:
        print("YES")
