t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if abs(x-z)>abs(y-z):
        print("Cat B")
    elif abs(x-z)<abs(y-z):
        print("Cat A")
    else:
        print("Mouse C")
