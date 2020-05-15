# Python3 program to find the minimum 
# number of swaps required to sort 
# the given array 

# Function to find minimum swaps 
def minimumSwaps(arr): 
	
	# Initialise count variable 
	count = 0; 
	i = 0; 
	while (i < len(arr)): 

		# If current element is 
		# not at the right position 
		if (arr[i] != i + 1): 

			while (arr[i] != i + 1): 
				temp = 0; 

				# Swap current element 
				# with correct position 
				# of that element 
				temp = arr[arr[i] - 1]; 
				arr[arr[i] - 1] = arr[i]; 
				arr[i] = temp; 
				count += 1; 
			
		# Increment for next index 
		# when current element is at 
		# correct position 
		i += 1; 
	
	return count; 

# Driver code 
if __name__ == '__main__': 
	arr = [ 2, 3, 4, 1, 5 ]; 

	# Function to find minimum swaps 
	print(minimumSwaps(arr)); 
	
# This code is contributed by 29AjayKumar 
