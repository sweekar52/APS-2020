def bc(n,k):
    if n==k or k==0:
        return 1
    return bc(n-1,k-1) + bc(n-1,k) 
print(bc(5,3))