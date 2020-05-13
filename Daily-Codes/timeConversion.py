s=list(input().split(":"))
flag=1
if s[2][2]=="P":
    s[0]=int(s[0])
    if s[0] != 12:
        s[0] += 12
    s[0] = str(s[0])
    
else:
    s[0]=int(s[0])
    if s[0] == 12:
        print("00",end=":")
        flag=0
    if s[0] < 10:
        print("0" + str(s[0]),end=":")
        flag=0


if flag:        
    print(s[0],end=":")
print(s[1],end=":")
print(s[2][0],end="")
print(s[2][1])
