def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if m==1:
    lcm=a[0]
else:
    lcm = find_lcm(a[0], a[1])
    for i in range(2, m): 
        lcm = find_lcm(lcm, a[i])  
m=min(b)
i=1
x=[]
y=lcm
while(y<=m):
    x.append(y)
    i += 1
    y = i * lcm
count=0
for i in range(len(x)):
    flag=1
    for j in range(n):
        if (b[j]%x[i])!=0:
            flag=0
    if flag:
        count += 1
print(count)


  