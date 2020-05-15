def eggDrop(n, k): 
	dp = [[0 for i in range(n + 1)] for j in range(k + 1)] 

	x = 0
	while (dp[x][n] < k): 
		x += 1
		for i in range(1, n + 1): 
			dp[x][i] = dp[x - 1][i - 1] + dp[x - 1][i] + 1
	
	return x

print(eggDrop(2, 36))