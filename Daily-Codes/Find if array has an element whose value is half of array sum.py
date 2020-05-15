# Python 3 program to check if array 
# has an element whose value is half 
# of array sum. 

# Function to check if answer exists 
def checkForElement(array, n): 
	
	# Sum of all array elements 
	sum = 0
	for i in range(n): 
		sum += array[i] 

	# If sum is odd 
	if (sum % 2): 
		return False

	sum //= 2	 # If sum is Even 

	# Do binary search for the 
	# required element 
	start = 0
	end = n - 1
	while (start <= end) : 
		mid = start + (end - start) // 2
		if (array[mid] == sum): 
			return True	
		elif (array[mid] > sum) : 
			end = mid - 1;	 
		else: 
			start = mid + 1

	return False

# Driver code 
if __name__ == "__main__": 
	array = [ 1, 2, 3 ] 
	n = len(array) 
	if (checkForElement(array, n)): 
		print("Yes") 
	else: 
		print("No") 

# This code is contributed 
# by ChitraNayal 
