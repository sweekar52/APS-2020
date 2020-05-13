n=int(input())
a=list(map(int,input().split()))
b=[]
b=a
a=set(a)
a=list(a)
a.sort()
b.sort()
max1=0
index=0
for i in range(len(a)):
    count=0
    for j in range(len(b)):
        if b[j]==a[i]:
            count += 1
    if max1 < count:
        max1=count
        index=i
print(a[index])
