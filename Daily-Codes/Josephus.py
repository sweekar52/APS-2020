def josephus(n,k):
    res=0
    for i in range(1,n+1):
        res = (res+k)%i
    return res + 1

n=7
k=2
print(josephus(n,k))