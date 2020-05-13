def maxSubArraySum(arr,s):  
    max_so_far =arr[0] 
    curr_max = arr[0] 
    for i in range(1,s): 
        curr_max = max(arr[i], curr_max + arr[i]) 
        max_so_far = max(max_so_far,curr_max)     
    return max_so_far
def maxSubsequence(arr,s):
    count=0
    flag=0
    for i in range(s):
        if arr[i]>0:
            count += arr[i]
            flag=1
    if flag==0:
        return max(arr)
    return count

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxSubArraySum(arr,n),maxSubsequence(arr,n))
