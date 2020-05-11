n=int(input("Enter the number "))
i=int(input("Enter the  value of i "))

n |= 1<<(i-1)
print(n)