x1,v1,x2,v2 = map(int,input().split())
if x2>x1 and v2>v1:
    print("NO")
elif abs(x1-x2) > 0 and v1 == v2:
    print("NO")
elif ((x1-x2)%(v2-v1))!=0:
    print("NO")
else:
    print("YES")
