n=int(input())
a=list(map(int,input().split()))

if sum(a)%2:
    print("NO")
else:
    print("YES")
    odd_count = len(list(filter(lambda x: (x%2 != 0) , a)))
    print(int(odd_count/2))