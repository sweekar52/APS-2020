n=int(input())
x=[]
for i in input().split():
    x.append(i)
c=x.__len__()
a=0
while a<c:
    x[a]=int(x[a])
    a=a+1
x.sort()
i=0
count=0
while i<c:
    if x[i]==x[c-1]:
        count=count+1
    i=i+1
print(count)
