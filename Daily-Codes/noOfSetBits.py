n=int(input("Enter the number "))
count = 0
while(n):
    n &= n-1
    count += 1
print(count)