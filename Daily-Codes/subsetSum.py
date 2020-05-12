def subSetSum(arr, n, s):
    dp = [[False for j in range(s+1)] for i in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    dp[0][arr[0]] = True

    for i in range(1,n):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
    
    for i in dp:
        print(i)

def main():
    arr = [2,3,7,8,10]
    n = 5
    s = 11
    subSetSum(arr, n, s)

if __name__ == "__main__":
    main()