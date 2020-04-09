a=[1,2,3]
n=len(a)
i=1
x=[]
while i< 1<<n:
    temp=i
    j=0
    y=[]
    while(temp):
        if (temp&1):
            y.append(a[j])
        temp >>= 1;
        j += 1
    x.append(y)
    i += 1
print(x)
