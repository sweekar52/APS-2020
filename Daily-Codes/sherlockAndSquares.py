import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    a=math.ceil(math.sqrt(a))
    b=math.floor(math.sqrt(b))
    print(b-a+1)
