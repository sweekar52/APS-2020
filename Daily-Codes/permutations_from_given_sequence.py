# Python3 program to print two 
# permutations from a given sequence 

# Function to check if the sequence is 
# concatenation of two permutations or not 
def checkPermutation(arr, n): 
	# Computing the sum of all the 
	# elements in the array 
	sum = 0
	for i in range(n): 
		sum += arr[i] 

	# Computing the prefix sum 
	# for all the elements in the array 
	prefix = [0 for i in range(n+1)] 
	prefix[0] = arr[0] 
	for i in range(1,n): 
		prefix[i] = prefix[i - 1] + arr[i] 

	# Iterating through the i 
	# from lengths 1 to n-1 
	for i in range(n - 1): 
		
		# Sum of first i+1 elements 
		lsum = prefix[i] 

		# Sum of remaining n-i-1 elements 
		rsum = sum - prefix[i] 

		# Lengths of the 2 permutations 
		l_len = i + 1
		r_len = n - i - 1

		# Checking if the sums 
		# satisfy the formula or not 
		if (((2 * lsum) == (l_len * (l_len + 1))) and
				((2 * rsum) == (r_len * (r_len + 1)))): 
			return True

	return False

# Function to print the 
# two permutations 
def printPermutations(arr,n,l1,l2): 
	# Print the first permutation 
	for i in range(l1): 
		print(arr[i],end = " ") 

	print("\n",end = ""); 

	# Print the second permutation 
	for i in range(l1, n, 1): 
		print(arr[i], end = " ") 

# Function to find the two permutations 
# from the given sequence 
def findPermutations(arr,n): 
	
	# If the sequence is not a 
	# concatenation of two permutations 
	if (checkPermutation(arr, n) == False): 
		print("Not Possible") 
		return

	l1 = 0
	l2 = 0

	# Find the largest element in the 
	# array and set the lengths of the 
	# permutations accordingly 
	l1 = max(arr) 
	l2 = n - l1 

	s1 = set() 
	s2 = set() 
	for i in range(l1): 
		s1.add(arr[i]) 

	for i in range(l1,n): 
		s2.add(arr[i]) 

	if (len(s1) == l1 and len(s2) == l2): 
		printPermutations(arr, n, l1, l2) 
	else: 
		temp = l1 
		l1 = l2 
		l2 = temp 
		printPermutations(arr, n, l1, l2) 

# Driver code 
if __name__ == '__main__': 
	arr = [2, 1, 3, 4, 5,6, 7, 8, 9, 1,10, 2] 
	n = len(arr) 

	findPermutations(arr, n) 

# This code is contributed by Surendra_Gangwar 
