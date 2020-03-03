def root(a,i):
    while(a[i]!=i):
        i=a[i]
    return i

def weightedUnion(a,size,u,v):
    rootu=root(a,u)
    rootv=root(a,v)
    if(size[rootu]<size[rootv]):
        a[rootu]=a[rootv]
        size[rootv] += size[rootu]
    else:
        a[rootv]=a[rootu]
        size[rootu] += size[rootv]


a=[i for i in range(6)]
size=[1 for _ in range(len(a))]
weightedUnion(a,size,0,1)
weightedUnion(a,size,1,2)
weightedUnion(a,size,3,2)
print(size)