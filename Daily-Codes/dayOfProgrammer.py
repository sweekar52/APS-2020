n=int(input())
if n!=1918:
    if ((n%400) == 0 or (n%4 == 0 and n%100 !=0)) or (n<1918 and n%4 == 0) :
        print("12.09",end=".")
        print(n)
    else:
        print("13.09",end=".")
        print(n)
else:
    print("26.09.1918")

