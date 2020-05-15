# Python3 implementation of the approach 

# Function to return the kth element 
# in the modified array 
def getNumber(n, k): 
	arr = [0] * n; 

	i = 0; 

	# First odd number 
	odd = 1; 
	while (odd <= n): 
		
		# Insert the odd number 
		arr[i] = odd; 
		i += 1; 

		# Next odd number 
		odd += 2; 

	# First even number 
	even = 2; 
	while (even <= n): 
		# Insert the even number 
		arr[i] = even; 
		i += 1; 

		# Next even number 
		even += 2; 

	# Return the kth element 
	return arr[k - 1]; 

# Driver code 
if __name__ == '__main__': 
	n = 8; 
	k = 5; 
	print(getNumber(n, k)); 

# This code is contributed by Rajput-Ji 
