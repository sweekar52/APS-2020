# Python3 program to find minimum and 
# maximum prime number in given array. 
import math as mt 

# Function to find count of prime 
def Prime(arr, n): 

	# Find maximum value in the array 
	max_val = max(arr) 

	# USE SIEVE TO FIND ALL PRIME NUMBERS 
	# LESS THAN OR EQUAL TO max_val 
	# Create a boolean array "prime[0..n]". 
	# A value in prime[i] will finally be 
	# false if i is Not a prime, else true. 
	prime = [True for i in range(max_val + 1)] 

	# Remaining part of SIEVE 
	prime[0] = False
	prime[1] = False
	for p in range(2, mt.ceil(mt.sqrt(max_val))): 

		# If prime[p] is not changed, 
		# then it is a prime 
		if (prime[p] == True): 

			# Update all multiples of p 
			for i in range(2 * p, max_val + 1, p): 
					prime[i] = False
		
	# Minimum and Maximum prime number 
	minimum = 10**9
	maximum = -10**9
	for i in range(n): 
		if (prime[arr[i]] == True): 
			minimum = min(minimum, arr[i]) 
			maximum = max(maximum, arr[i]) 
		
	print("Minimum : ", minimum ) 
	print("Maximum : ", maximum ) 

# Driver code 
arr = [1, 2, 3, 4, 5, 6, 7] 
n = len(arr) 

Prime(arr, n) 

# This code is contributed by 
# Mohit kumar 29 
