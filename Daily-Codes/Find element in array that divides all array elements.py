# Python3 program to find such number 
# in the array that all array 
# elements are divisible by it 

# Returns GCD of two numbers 
def gcd (a, b) : 
	if (a == 0) : 
		return b 
	
	return gcd (b % a, a) 
	
# Function to return the desired 
# number if exists 
def findNumber (arr, n) : 

	# Find GCD of array 
	ans = arr[0] 
	for i in range(0, n) : 
		ans = gcd (ans, arr[i]) 
		
	# Check if GCD is present in array 
	for i in range(0, n) : 
		if (arr[i] == ans) : 
			return ans 
	
	return -1
	
# Driver Code 
arr = [2, 2, 4]; 
n = len(arr) 
print(findNumber(arr, n)) 

# This code is contributed by Nikita Tiwari 
