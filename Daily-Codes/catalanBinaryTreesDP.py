def catalan_binary_trees(n):
    c=[0 for _ in range(n+1)]
    c[0]=1
    c[1]=1
    c[2]=2
    for i in range(3,n+1):
        for j in range(i):
            c[i] += c[j] * c[(i-1)-j]
    return c[n]

n=3
print(catalan_binary_trees(n))