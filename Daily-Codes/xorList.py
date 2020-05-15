# Python3 program to find the XOR of 
# all elements in the array 

# Function to find the XOR of 
# all elements in the array 
def xorOfArray(arr, n): 

	# Resultant variable 
	xor_arr = 0

	# Iterating through every element in 
	# the array 
	for i in range(n): 

		# Find XOR with the result 
		xor_arr = xor_arr ^ arr[i] 

	# Return the XOR 
	return xor_arr 

# Driver Code 
if __name__ == '__main__': 
	arr = [3, 9, 12, 13, 15] 
	n = len(arr) 

	# Function call 
	print(xorOfArray(arr, n)) 

# This code is contributed by mohit kumar 29 
