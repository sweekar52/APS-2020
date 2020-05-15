# Python 3 program to count the 
# number of ways to change 
# the direction of edges 
# such that no cycle is 
# present in the graph 

# List cycles[] to store 
# the cycle with vertices 
# associated with each cycle 
cycles = [] 

# Function to count the 
# number of vertices in the 
# current cycle 
def DFSUtil(u, arr, vis, cyclecnt): 

	cycles[cyclecnt] += 1
	vis[u] = 3

	# Returns when the same 
	# initial vertex is found 
	if (vis[arr[u]] == 3) : 
		return

	# Recurr for next vertex 
	DFSUtil(arr[u], arr, vis, cyclecnt) 

# DFS traversal to detect 
# the cycle in graph 
def DFS( u, arr, vis, cyclecnt): 

	# Marke vis[u] to 2 to 
	# check for any cycle form 
	vis[u] = 2

	# If the vertex arr[u] 
	# is not visited 
	if (vis[arr[u]] == 0) : 
		
		# Call DFS 
		DFS(arr[u], arr, vis, cyclecnt) 

	# If current node is 
	# processed 
	elif (vis[arr[u]] == 1): 
		vis[u] = 1
		return

	# Cycle found, call DFSUtil 
	# to count the number of 
	# vertices in the current 
	# cycle 
	else : 
		cycles.append(0) 

		# Count number of 
		# vertices in cycle 
		DFSUtil(u, arr, vis,cyclecnt) 
		cyclecnt += 1

	# Current Node is processed 
	vis[u] = 1

# Function to count the 
# number of ways 
def countWays(arr, N,cyclecnt): 

	ans = 1

	# To precompute the power 
	# of 2 
	dp = [0]*(N + 1) 
	dp[0] = 1

	# Storing power of 2 
	for i in range(1, N + 1): 
		dp[i] = (dp[i - 1] * 2) 

	# Array vis[] created for 
	# DFS traversal 
	vis = [0]*(N + 1) 

	# DFS traversal from Node 1 
	for i in range(1, N + 1) : 
		if (vis[i] == 0) : 

			# Calling DFS 
			DFS(i, arr, vis, cyclecnt) 

	cnt = N 

	# Traverse the cycles array 
	for i in range(len(cycles)) : 

		# Remove the vertices 
		# which are part of a 
		# cycle 
		cnt -= cycles[i] 

		# Count form by number 
		# vertices form cycle 
		ans *= dp[cycles[i]] - 2

	# Count form by number of 
	# vertices not forming 
	# cycle 
	ans = (ans * dp[cnt]) 

	return ans 

# Driver's Code 
if __name__ == "__main__": 
	
	N = 3
	cyclecnt = 0
	arr = [ 0, 2, 3, 1 ] 

	# Function to count ways 
	print(countWays(arr, N,cyclecnt)) 
	
# This code is contributed by chitranayal 
