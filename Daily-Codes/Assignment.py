def count_set_bits(n):
    count=0
    while(n):
        n= n & (n-1)
        count += 1
    return count


arr=[[3,2,7],[5,1,3],[2,7,2]]
dp=[float('inf') for _ in range(1<<len(arr))]
dp[0]=0
for mask in range(1<<len(arr)):
    x=count_set_bits(mask)
    for j in range(len(arr)):
        if mask & (1<<j):
            pass
        else:
            dp[mask|(1<<j)] = min(dp[mask|(1<<j)],dp[mask]+arr[x][j])
print(dp)
print()
print(dp[(1<<len(arr))-1])