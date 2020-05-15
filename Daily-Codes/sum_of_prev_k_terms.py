
def sumOfPrevK(N, K):  
    arr = [0 for i in range(N)]  
    arr[0] = 1
  
    # Pick a starting point 
    for i in range(1,N):  
        j = i - 1
        count = 0
        sum = 0
          
        # Find the sum of all  
        # elements till count < K  
        while (j >= 0 and count < K): 
            sum = sum + arr[j] 
            j = j - 1
            count = count + 1
  
        # Find the value of  
        # sum at i position  
        arr[i] = sum
  
    for i in range(0, N):  
        print(arr[i]) 
  
# Driver Code  
N = 10
K = 4
sumOfPrevK(N, K) 