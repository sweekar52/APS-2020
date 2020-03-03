def bc(n,k):
    c=[0 for _ in range(n-1)]
    c[0]=1
    for i in range(n):
        for j in range(min(i,k),0,-1):
            c[j] += c[j-1]
    return c[k]

print(bc(3,2))