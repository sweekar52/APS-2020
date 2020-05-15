# Python program to find the element having 
# different frequency than other array 
# elements having same frequency 

# Function for above implementation 
def findElement(arr, n) : 
	
	# Empty dictionary to hold the values 
	freq = {} 
	
	# Initialization of frequencies of each 
	# element to 0 
	for i in range(0, n) : 
		
		freq[arr[i]] = 0
		
	# Count of frequencies of elements 
	for i in range(0, n) : 
		
		freq[arr[i]] = freq[arr[i]] + 1
	
	# Storing the first value of dictionary 
	trd_ele = freq[0] 
	
	# Variable to hold the final result 
	position = -1
	
	# Following loop iterates through the dictionary 
	# and checks if frequencies are different 
	# from the frequency of the first element 
	for i in freq : 
		
		flag = freq[i] 
		
		if trd_ele != flag : 
			
			# Difference has been detected 
			position = i 
			break
			
	# Following lines of code checks if the first 
	# element is itself the required anomaly by 
	# comparing the frequencies of first 3 elements 
	fst_ele = freq[1] 
	sec_ele = freq[2] 
	
	if trd_ele != fst_ele : 
		
		if trd_ele != sec_ele : 
			
			for i in freq : 
				
				# First element is the desired result 
				position = i 
				break
	
	# Final result is returned 
	return position 
	

# Driver code 
arr = [ 0, 1, 2, 4, 4 ] 
# Variable to store length of array 
n = len(arr) 
print (findElement(arr, n)) 

# This code is contributed by Pratik Basu 
