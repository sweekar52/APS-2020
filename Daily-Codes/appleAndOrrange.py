s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

count1=0
count2=0
for i in x:
    if ((a+i) >= s) and ((a+i) <= t):
        count1 += 1


for i in y:
    if ((b+i) >= s) and ((b+i) <= t):
        count2 += 1
print(count1)
print(count2)
