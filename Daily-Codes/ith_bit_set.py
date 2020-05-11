n=int(input("Enter the number "))
i=int(input("Enter the value of i "))
if n & (1<<(i-1)):
    print("Yes")
else:
    print("No")