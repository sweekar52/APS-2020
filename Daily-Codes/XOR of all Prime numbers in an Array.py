# Python3 program to find Xor of 
# all Prime numbers in array 

prime = [True] * (100005) 

def SieveOfEratosthenes(n): 

	# False here indicates 
	# that it is not prime 
	prime[1] = False
	p = 2
	
	while p*p <= n: 

		# If prime[p] is not changed, 
		# then it is a prime 
		if prime[p]: 

			# Update all multiples of p, 
			# set them to non-prime 
			for i in range(p * 2, n+1, p): 
				prime[i] = False
				
		p += 1
		
# Function to compute xor 
# of all prime elements 
def xorPrimes(arr, n): 

	SieveOfEratosthenes(100004) 

	xorVal = 0
	for i in range(0, n): 

		# if the element is prime 
		if prime[arr[i]]: 
			xorVal = xorVal ^ arr[i] 
	
	return xorVal 

# Driver code 
if __name__ == "__main__": 

	arr = [4, 3, 2, 6, 100, 17] 
	n = len(arr) 

	print(xorPrimes(arr, n)) 

# This code is contributed by Rituraj Jain 
