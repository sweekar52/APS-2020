# Python3 implementation of the approach 

# Function to return the bitwise AND of the 
# sum of primes and the sum of non-primes 
def calculateAND(arr, n): 
	
	# Find maximum value in the array 
	max_val = max(arr) 

	# USE SIEVE TO FIND ALL PRIME NUMBERS 
	# LESS THAN OR EQUAL TO max_val 
	# Create a boolean array "prime[0..n]". 
	# A value in prime[i] will finally be false 
	# if i is Not a prime, else true. 
	prime = [True for i in range(max_val + 1)] 

	# Remaining part of SIEVE 
	prime[0] = False
	prime[1] = False
	for p in range(2, max_val + 1): 

		if p * p >= max_val: 
			break

		# If prime[p] is not changed, 
		# then it is a prime 
		if (prime[p]): 

			# Update all multiples of p 
			for i in range(2 * p, max_val + 1, p): 
				prime[i] = False

	# Store the sum of primes in S1 and 
	# the sum of non-primes in S2 
	S1 = 0
	S2 = 0
	for i in range(n): 

		if (prime[arr[i]]): 

			# The number is prime 
			S1 += arr[i] 
		elif (arr[i] != 1): 

			# The number is not prime 
			S2 += arr[i] 

	# Return the bitwise AND of the sums 
	return (S1 & S2) 

# Driver code 
arr = [3, 4, 6, 7] 
n = len(arr) 

print(calculateAND(arr, n)) 

# This code is contributed by Mohit Kumar 
