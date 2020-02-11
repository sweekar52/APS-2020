n=int(input())
a=[0 for _ in range(n+1) ]
a[0]=1
x=[3,5,10]
for i in x:
    for j in range(i,n+1):
        a[j]=a[j] + a[j-i]
#print(a)

f=[[0] for _ in range(n+1)]
a.reverse()
x.reverse()
print(a)
for i in x:
    k=i
    for j in range(n+1):
        if a[j]>0:
            while(a[k+j]>0):
                f[j].append(i)
                if (k+j <n):
                    k = k+j
                else:
                    break    
            a[j]=a[j]-1
f.reverse()
print(f)

