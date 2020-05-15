# Python3 implementation of the approach 
sz = 10**5
isPrime = [True for i in range(sz + 1)] 

# Function for Sieve of Eratosthenes 
def sieve(): 
	
	isPrime[0] = isPrime[1] = False

	i = 2
	while i * i < sz: 
		if (isPrime[i]): 
			for j in range(i * i, sz, i): 
				isPrime[j] = False
		i += 1

# Function to pr the elements of the array 
def prArray(arr, lenn): 
	for i in range(lenn): 
		print(arr[i], end = " ") 

# Function to remove all the prime numbers 
def removePrimes(arr, lenn): 
	
	# Generate primes 
	sieve() 

	# Traverse the array 
	i = 0
	while i < lenn: 

		# If the current element is prime 
		if (isPrime[arr[i]]): 

			# Shift all the elements on the 
			# right of it to the left 
			for j in range(i, lenn - 1): 
				arr[j] = arr[j + 1] 

			# Decrease the loop counter by 1 
			# to check the shifted element 
			i -= 1

			# Decrease the lenngth 
			lenn -= 1

		i += 1

	# Pr the updated array 
	prArray(arr, lenn) 

# Driver code 
if __name__ == '__main__': 
	arr = [4, 6, 5, 3, 8, 7, 10, 11, 14, 15] 
	lenn = len(arr) 

	removePrimes(arr, lenn) 

# This code is contributed by Mohit Kumar 
